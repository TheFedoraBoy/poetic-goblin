/* ═══════════════════════════════════════════════════════════════════════
   Poetic Goblin — Client-Side JavaScript
   ═══════════════════════════════════════════════════════════════════════ */

// ─── Dark Mode (global, outside DOMContentLoaded for early access) ───
function toggleDarkMode() {
    const isDark = document.body.classList.toggle('dark-mode');
    localStorage.setItem('pg-theme', isDark ? 'dark' : 'light');
    // Update toggle switch if it exists
    const toggle = document.getElementById('dark-mode-toggle');
    if (toggle) toggle.classList.toggle('active', isDark);
}

// Init toggle state on page load
document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('dark-mode-toggle');
    if (toggle && document.body.classList.contains('dark-mode')) {
        toggle.classList.add('active');
    }
});

document.addEventListener('DOMContentLoaded', () => {

    // ─── CSRF Token Helper ────────────────────────────────────────────
    function getCsrfToken() {
        const meta = document.querySelector('meta[name="csrf-token"]');
        return meta ? meta.getAttribute('content') : '';
    }

    // ─── Flash Messages Auto-dismiss ─────────────────────────────────
    document.querySelectorAll('.flash').forEach(f => {
        f.addEventListener('click', () => { f.style.opacity = '0'; setTimeout(() => f.remove(), 300); });
        setTimeout(() => { f.style.opacity = '0'; setTimeout(() => f.remove(), 300); }, 5000);
    });

    // ─── Like Buttons ────────────────────────────────────────────────
    document.querySelectorAll('.like-btn').forEach(btn => {
        btn.addEventListener('click', async () => {
            const postId = btn.dataset.postId;
            try {
                const res = await fetch(`/post/${postId}/like`, {
                    method: 'POST',
                    headers: { 'X-Requested-With': 'XMLHttpRequest' }
                });
                const data = await res.json();
                const icon = btn.querySelector('.icon');
                const count = btn.querySelector('.count');
                if (data.liked) {
                    btn.classList.add('liked');
                    icon.textContent = '🔥';
                } else {
                    btn.classList.remove('liked');
                    icon.textContent = '🤍';
                }
                count.textContent = data.count || '';
            } catch (e) { console.error(e); }
        });
    });

    // ─── Comment Toggle ──────────────────────────────────────────────
    document.querySelectorAll('.comment-toggle-btn').forEach(btn => {
        btn.addEventListener('click', async () => {
            const postId = btn.dataset.postId;
            const section = document.getElementById(`comments-${postId}`);
            if (!section) return;

            const isOpen = section.classList.contains('open');
            if (isOpen) {
                section.classList.remove('open');
                return;
            }

            // Load comments
            try {
                const res = await fetch(`/post/${postId}/comments`);
                const comments = await res.json();
                const list = section.querySelector('.comments-list');
                list.innerHTML = comments.map(c => renderComment(c)).join('');
                section.classList.add('open');
            } catch (e) { console.error(e); }
        });
    });

    // ─── Comment Submit ──────────────────────────────────────────────
    document.querySelectorAll('.comment-submit-btn').forEach(btn => {
        btn.addEventListener('click', () => submitComment(btn.dataset.postId));
    });
    document.querySelectorAll('.comment-input').forEach(inp => {
        inp.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                submitComment(inp.dataset.postId);
            }
        });
    });

    async function submitComment(postId) {
        const inp = document.getElementById(`comment-input-${postId}`);
        if (!inp) return;
        const content = inp.value.trim();
        if (!content) return;
        const formData = new FormData();
        formData.append('content', content);
        try {
            const res = await fetch(`/post/${postId}/comment`, {
                method: 'POST',
                body: formData,
                headers: { 'X-Requested-With': 'XMLHttpRequest' }
            });
            const data = await res.json();
            if (data.error) return;
            const list = document.querySelector(`#comments-${postId} .comments-list`);
            list.insertAdjacentHTML('beforeend', renderComment(data));
            inp.value = '';
            // Update count
            const countEl = document.querySelector(`.comment-toggle-btn[data-post-id="${postId}"] .count`);
            if (countEl) countEl.textContent = (parseInt(countEl.textContent) || 0) + 1;
        } catch (e) { console.error(e); }
    }

    function renderComment(c) {
        const initial = (c.author || '?')[0].toUpperCase();
        const avatarHtml = c.avatar_url
            ? `<img src="${c.avatar_url}" class="comment-avatar" alt="">`
            : `<div class="comment-avatar avatar-placeholder" style="width:28px;height:28px;font-size:0.65rem;">${initial}</div>`;
        return `<div class="comment" data-comment-id="${c.id}">
            ${avatarHtml}
            <div class="comment-body">
                <a href="/profile/${c.username}" class="comment-author">${escapeHtml(c.author)}</a>
                <div class="comment-text">${escapeHtml(c.content)}</div>
                <div class="comment-time">${c.created_at}</div>
            </div>
        </div>`;
    }

    // ─── Comment Delete ──────────────────────────────────────────────
    document.addEventListener('click', async (e) => {
        const btn = e.target.closest('.comment-delete-btn');
        if (!btn) return;
        const commentId = btn.dataset.commentId;
        if (!confirm('Delete this comment?')) return;
        try {
            const res = await fetch(`/comment/${commentId}/delete`, {
                method: 'POST',
                headers: { 'X-Requested-With': 'XMLHttpRequest' }
            });
            const data = await res.json();
            if (data.deleted) {
                const comment = btn.closest('.comment');
                if (comment) { comment.style.opacity = '0'; setTimeout(() => comment.remove(), 300); }
            }
        } catch (e) { console.error(e); }
    });

    // ─── Follow Buttons ──────────────────────────────────────────────
    document.querySelectorAll('.follow-btn').forEach(btn => {
        btn.addEventListener('click', async () => {
            const username = btn.dataset.username;
            try {
                const res = await fetch(`/follow/${username}`, {
                    method: 'POST',
                    headers: { 'X-Requested-With': 'XMLHttpRequest' }
                });
                const data = await res.json();
                if (data.following) {
                    btn.textContent = 'Following';
                    btn.classList.add('following');
                    btn.classList.remove('btn-primary');
                } else {
                    btn.textContent = 'Follow';
                    btn.classList.remove('following');
                    btn.classList.add('btn-primary');
                }
                const fc = document.getElementById('follower-count');
                if (fc) fc.textContent = data.follower_count;
            } catch (e) { console.error(e); }
        });
    });

    // ─── Campaign Session Expand ─────────────────────────────────────
    document.querySelectorAll('.session-expand-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const postId = btn.dataset.postId;
            const hidden = document.querySelectorAll(`.session-item[data-post-id="${postId}"].hidden-session`);
            hidden.forEach(s => s.style.display = 'block');
            btn.style.display = 'none';
        });
    });

    // ─── Escape HTML ─────────────────────────────────────────────────
    function escapeHtml(str) {
        const div = document.createElement('div');
        div.textContent = str;
        return div.innerHTML;
    }
});
