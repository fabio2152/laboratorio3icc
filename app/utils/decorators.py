from functools import wraps
from flask import abort
from flask_login import current_user


def admin_required(f):
    """Restringe la vista a usuarios con rol 'admin'. Requiere @login_required previo."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated
