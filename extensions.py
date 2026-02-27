"""
Poetic Goblin — Flask Extensions
Initialized here, bound to app in app.py via init_app().
"""

try:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address
    limiter = Limiter(get_remote_address, storage_uri="memory://")
except ImportError:
    print("[Poetic Goblin] flask-limiter not installed. Rate limiting disabled.")
    class _NoOpLimiter:
        def limit(self, *a, **kw):
            def decorator(f): return f
            return decorator
        def exempt(self, f): return f
        def init_app(self, app): pass
    limiter = _NoOpLimiter()
