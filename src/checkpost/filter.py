
import functools
from flask import request

class Filter():
         
    def enable_api_security(func):
        @functools.wraps(func)
        def decorator(*args, **kwargs):
            if isAuthorizationHeaderPresent():
                return func(*args, **kwargs)
            else:
                return {"message":"Authorization header not present"},300
        return decorator


def isAuthorizationHeaderPresent():
        if request.headers.get("Authorization"):
            return True
        else:
            return False