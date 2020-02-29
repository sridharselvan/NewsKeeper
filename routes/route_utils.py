from flask import session
from functools import wraps


def common_route(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        session_obj = session['item']
        kwargs['is_session_valid'] = True
        if not session_obj:
            kwargs['is_session_valid'] = False
        else:
            return fn(*args, **kwargs)
    return wrapper