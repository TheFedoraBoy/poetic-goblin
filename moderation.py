"""
Poetic Goblin — Content Moderation
Three layers of protection:

1. PROFANITY FILTER (local, instant)
   - Censors swear words with asterisks on display
   - Users can toggle this off in Settings (show_explicit)
   - Stored as-is in DB, filtered at render time

2. HATE SPEECH DETECTION (Perspective API by Google/Jigsaw)
   - Blocks content creation if toxicity score exceeds threshold
   - NOT toggleable — hate speech is always blocked
   - Free API: https://perspectiveapi.com/

3. IMAGE MODERATION (AWS Rekognition)
   - Blocks NSFW image uploads before saving to S3
   - NOT toggleable — explicit images are always blocked
   - Uses existing AWS credentials

Set PERSPECTIVE_API_KEY and MODERATION_ENABLED in env vars.
"""

import re
import io
from config import Config

# ─── Profanity Word List ────────────────────────────────────────────────────
# Common profanity for the asterisk filter. This is the "toggleable" layer —
# users who enable show_explicit will see these words uncensored.
# Hate speech / slurs are handled separately by the Perspective API and are
# ALWAYS blocked regardless of user settings.

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
# Word boundary matching, case insensitive
_profanity_pattern = None


def _get_profanity_pattern():
    """Lazily compile the profanity regex pattern."""
    global _profanity_pattern
    if _profanity_pattern is None:
        # Sort by length (longest first) so "motherfucker" matches before "fuck"
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
    """Check if text contains any profanity words. Returns True/False."""
    if not text:
        return False
    pattern = _get_profanity_pattern()
    return bool(pattern.search(text))


# ─── Hate Speech Detection (Perspective API) ───────────────────────────────

def check_hate_speech(text):
    """
    Check text for hate speech using Google's Perspective API.
    Returns a dict with scores, or None if the API is unavailable.

    Scores are 0.0 - 1.0 for each attribute:
      - TOXICITY: rude, disrespectful, or unreasonable
      - SEVERE_TOXICITY: very hateful, aggressive, or disrespectful
      - IDENTITY_ATTACK: negative or hateful against an identity group
      - THREAT: intention to inflict pain or violence
      - SEXUALLY_EXPLICIT: contains sexual content

    Returns None if API key not set or API call fails (fail-open).
    """
    api_key = Config.PERSPECTIVE_API_KEY
    if not api_key or not Config.MODERATION_ENABLED:
        return None

    if not text or len(text.strip()) < 3:
        return None

    try:
        import urllib.request
        import urllib.error
        import json

        url = f'https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze?key={api_key}'

        payload = {
            'comment': {'text': text[:3000]},  # API limit
            'languages': ['en'],
            'requestedAttributes': {
                'TOXICITY': {},
                'SEVERE_TOXICITY': {},
                'IDENTITY_ATTACK': {},
                'THREAT': {},
                'SEXUALLY_EXPLICIT': {},
            }
        }

        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(
            url,
            data=data,
            headers={
                'Content-Type': 'application/json',
                'User-Agent': 'PoeticGoblin/1.0',
            },
            method='POST',
        )

        with urllib.request.urlopen(req, timeout=5) as resp:
            result = json.loads(resp.read().decode('utf-8'))

        scores = {}
        for attr, data in result.get('attributeScores', {}).items():
            scores[attr] = data['summaryScore']['value']

        return scores

    except Exception as e:
        print(f"[Poetic Goblin] Perspective API error (fail-open): {e}")
        return None


def is_text_allowed(text):
    """
    Check if text passes hate speech moderation.
    Returns (allowed: bool, reason: str or None).

    This is the BLOCKING check — hate speech is never allowed regardless of
    user settings. Regular profanity is handled separately by the display filter.
    """
    if not Config.MODERATION_ENABLED:
        return True, None

    scores = check_hate_speech(text)
    if scores is None:
        # API unavailable — fail open (allow content)
        return True, None

    threshold = Config.HATE_SPEECH_THRESHOLD

    # Check the most critical attributes
    if scores.get('SEVERE_TOXICITY', 0) >= threshold:
        return False, 'Your content was flagged for severe toxicity. Please revise and try again.'

    if scores.get('IDENTITY_ATTACK', 0) >= threshold:
        return False, 'Your content was flagged for targeting an identity group. Please revise and try again.'

    if scores.get('THREAT', 0) >= threshold:
        return False, 'Your content was flagged for containing threats. Please revise and try again.'

    # SEXUALLY_EXPLICIT at a slightly higher threshold (fantasy content can trip this)
    if scores.get('SEXUALLY_EXPLICIT', 0) >= min(threshold + 0.1, 0.95):
        return False, 'Your content was flagged for explicit sexual content. Please revise and try again.'

    # General TOXICITY at a slightly higher threshold (to allow heated in-character dialogue)
    if scores.get('TOXICITY', 0) >= min(threshold + 0.15, 0.95):
        return False, 'Your content was flagged as highly toxic. Please revise and try again.'

    return True, None


# ─── Image Moderation (AWS Rekognition) ─────────────────────────────────────

def check_image_safety(file_obj):
    """
    Check an image for NSFW content using AWS Rekognition.
    Returns (safe: bool, reason: str or None).

    Reads the file object, checks it, then seeks back to 0 so it can still
    be saved afterward.
    """
    if not Config.IMAGE_MODERATION_ENABLED:
        return True, None

    if not Config.AWS_ACCESS_KEY_ID or not Config.AWS_SECRET_ACCESS_KEY:
        print("[Poetic Goblin] AWS credentials not set. Image moderation skipped.")
        return True, None

    try:
        import boto3

        image_bytes = file_obj.read()
        file_obj.seek(0)  # Reset for subsequent save

        # Max 5MB for Rekognition inline
        if len(image_bytes) > 5 * 1024 * 1024:
            print("[Poetic Goblin] Image too large for Rekognition inline check. Skipping.")
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
                print(f"[Poetic Goblin] Image blocked: {label_name} ({confidence:.0f}% confidence)")
                return False, 'This image was flagged as containing explicit content and cannot be uploaded.'

        return True, None

    except ImportError:
        print("[Poetic Goblin] boto3 not installed. Image moderation skipped.")
        return True, None
    except Exception as e:
        print(f"[Poetic Goblin] Rekognition error (fail-open): {e}")
        return True, None  # Fail open
