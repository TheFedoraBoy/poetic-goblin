"""
Poetic Goblin — Content Moderation
Three layers of protection:

1. PROFANITY FILTER (local, instant)
   - Censors swear words with asterisks on display
   - Users can toggle this off in Settings (show_explicit)
   - Stored as-is in DB, filtered at render time

2. HATE SPEECH / HARMFUL CONTENT DETECTION (OpenAI Moderation API)
   - Blocks content creation if flagged for hate, harassment, violence, etc.
   - NOT toggleable — harmful content is always blocked
   - Free API: https://platform.openai.com/docs/guides/moderation
   - Requires OPENAI_API_KEY env var

3. IMAGE MODERATION (AWS Rekognition)
   - Blocks NSFW image uploads before saving to S3
   - NOT toggleable — explicit images are always blocked
   - Uses existing AWS credentials

Set OPENAI_API_KEY and MODERATION_ENABLED in env vars.
"""

import re
import io
from config import Config

# ─── Profanity Word List ────────────────────────────────────────────────────
# Common profanity for the asterisk filter. This is the "toggleable" layer —
# users who enable show_explicit will see these words uncensored.
# Hate speech / slurs are handled separately by the OpenAI Moderation API and
# are ALWAYS blocked regardless of user settings.

PROFANITY_WORDS = [
    # Common profanity
    'fuck', 'fucking', 'fucked', 'fucker', 'fuckers', 'fucks', 'motherfucker',
    'motherfucking', 'motherfuckers',
    'shit', 'shitting', 'shitty', 'shits', 'bullshit', 'horseshit', 'dipshit',
    'ass', 'asshole', 'assholes', 'asses', 'dumbass', 'jackass', 'badass',
    'bitch', 'bitches', 'bitching', 'bitchy',
    'damn', 'damned', 'dammit', 'goddamn', 'goddammit',
    'hell', 'hellhole',
    'crap', 'crappy',
    'dick', 'dicks', 'dickhead', 'dickheads',
    'cock', 'cocks', 'cocksucker',
    'pussy', 'pussies',
    'bastard', 'bastards',
    'piss', 'pissed', 'pissing',
    'whore', 'whores',
    'slut', 'sluts', 'slutty',
    'cunt', 'cunts',
    'tits', 'titty', 'titties',
    'wanker', 'wankers',
    'twat', 'twats',
    'bollocks',
    'arse', 'arsehole',
    'douche', 'douchebag', 'douchebags',
    'jerkoff',
]

# Build a compiled regex for fast matching
_profanity_pattern = None


def _get_profanity_pattern():
    """Lazily compile the profanity regex pattern."""
    global _profanity_pattern
    if _profanity_pattern is None:
        sorted_words = sorted(PROFANITY_WORDS, key=len, reverse=True)
        escaped = [re.escape(w) for w in sorted_words]
        _profanity_pattern = re.compile(
            r'\b(' + '|'.join(escaped) + r')\b',
            re.IGNORECASE
        )
    return _profanity_pattern


def censor_text(text):
    """
    Replace profanity with asterisks, preserving first and last letter.
    'fucking' -> 'f*****g', 'shit' -> 's**t', 'ass' -> 'a*s'
    """
    if not text:
        return text

    pattern = _get_profanity_pattern()

    def _replace(match):
        word = match.group(0)
        if len(word) <= 2:
            return '*' * len(word)
        elif len(word) == 3:
            return word[0] + '*' + word[2]
        else:
            return word[0] + '*' * (len(word) - 2) + word[-1]

    return pattern.sub(_replace, text)


def contains_profanity(text):
    """Check if text contains any profanity words."""
    if not text:
        return False
    pattern = _get_profanity_pattern()
    return bool(pattern.search(text))


# ─── Harmful Content Detection (OpenAI Moderation API) ─────────────────────

def check_moderation(text):
    """
    Check text for harmful content using OpenAI's free Moderation API.

    Categories: hate, hate/threatening, harassment, harassment/threatening,
    self-harm, sexual, sexual/minors, violence, violence/graphic.

    Returns the first result dict, or None if unavailable.
    """
    api_key = Config.OPENAI_API_KEY
    if not api_key or not Config.MODERATION_ENABLED:
        return None

    if not text or len(text.strip()) < 3:
        return None

    try:
        import urllib.request
        import urllib.error
        import json

        payload = {
            'model': 'omni-moderation-latest',
            'input': text[:10000],
        }

        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(
            'https://api.openai.com/v1/moderations',
            data=data,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}',
                'User-Agent': 'PoeticGoblin/1.0',
            },
            method='POST',
        )

        with urllib.request.urlopen(req, timeout=5) as resp:
            result = json.loads(resp.read().decode('utf-8'))

        if result.get('results'):
            return result['results'][0]
        return None

    except Exception as e:
        print(f"[Poetic Goblin] OpenAI Moderation API error (fail-open): {e}")
        return None


def is_text_allowed(text):
    """
    Check if text passes harmful content moderation.
    Returns (allowed: bool, reason: str or None).

    Harmful content is ALWAYS blocked regardless of user settings.
    Regular profanity is handled separately by the display censor filter.

    Violence threshold is set higher (0.9) since this is a fantasy/D&D platform
    where combat descriptions are normal.
    """
    if not Config.MODERATION_ENABLED:
        return True, None

    result = check_moderation(text)
    if result is None:
        return True, None  # Fail open

    if not result.get('flagged', False):
        return True, None

    categories = result.get('categories', {})
    scores = result.get('category_scores', {})

    # Hate speech — always block
    if categories.get('hate') or categories.get('hate/threatening'):
        return False, 'Your content was flagged for hateful language. Please revise and try again.'

    # Harassment — always block
    if categories.get('harassment') or categories.get('harassment/threatening'):
        return False, 'Your content was flagged for harassment. Please revise and try again.'

    # Sexual content — always block
    if categories.get('sexual') or categories.get('sexual/minors'):
        return False, 'Your content was flagged for sexual content. Please revise and try again.'

    # Self-harm — always block
    if categories.get('self-harm') or categories.get('self-harm/intent') or categories.get('self-harm/instructions'):
        return False, 'Your content was flagged for self-harm content. Please revise and try again.'

    # Violence — higher threshold for fantasy/D&D platform
    if categories.get('violence') or categories.get('violence/graphic'):
        violence_score = scores.get('violence', 0)
        graphic_score = scores.get('violence/graphic', 0)
        if violence_score > 0.9 or graphic_score > 0.85:
            return False, 'Your content was flagged for extreme violence. Please revise and try again.'
        return True, None  # Allow moderate fantasy violence

    # Flagged for something else — check if it's only violence-related
    flagged_cats = [k for k, v in categories.items() if v]
    if all('violence' in c for c in flagged_cats):
        return True, None

    return False, 'Your content was flagged as potentially harmful. Please revise and try again.'


# ─── Image Moderation (AWS Rekognition) ─────────────────────────────────────

def check_image_safety(file_obj):
    """
    Check an image for NSFW content using AWS Rekognition.
    Returns (safe: bool, reason: str or None).
    """
    if not Config.IMAGE_MODERATION_ENABLED:
        return True, None

    if not Config.AWS_ACCESS_KEY_ID or not Config.AWS_SECRET_ACCESS_KEY:
        print("[Poetic Goblin] AWS credentials not set. Image moderation skipped.")
        return True, None

    try:
        import boto3

        image_bytes = file_obj.read()
        file_obj.seek(0)

        if len(image_bytes) > 5 * 1024 * 1024:
            print("[Poetic Goblin] Image too large for Rekognition. Skipping.")
            return True, None

        client = boto3.client(
            'rekognition',
            aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
            region_name=Config.AWS_S3_REGION,
        )

        response = client.detect_moderation_labels(
            Image={'Bytes': image_bytes},
            MinConfidence=60,
        )

        blocked_categories = {
            'Explicit Nudity', 'Nudity', 'Graphic Male Nudity',
            'Graphic Female Nudity', 'Sexual Activity', 'Illustrated Explicit Nudity',
            'Adult Toys', 'Non-Explicit Nudity of Intimate parts and Coverage',
        }

        for label in response.get('ModerationLabels', []):
            label_name = label.get('Name', '')
            parent_name = label.get('ParentName', '')
            confidence = label.get('Confidence', 0)

            if (label_name in blocked_categories or parent_name in blocked_categories) and confidence >= 75:
                print(f"[Poetic Goblin] Image blocked: {label_name} ({confidence:.0f}%)")
                return False, 'This image was flagged as containing explicit content and cannot be uploaded.'

        return True, None

    except ImportError:
        print("[Poetic Goblin] boto3 not installed. Image moderation skipped.")
        return True, None
    except Exception as e:
        print(f"[Poetic Goblin] Rekognition error (fail-open): {e}")
        return True, None
