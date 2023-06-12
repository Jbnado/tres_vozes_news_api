import jwt
from flask import request, make_response, current_app
from functools import wraps
from jwt.exceptions import DecodeError, ExpiredSignatureError


def isAdmin(adminRequired=True):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                # Get token from the "Authorization" header
                token = request.headers.get("Authorization")
                if not token:
                    return make_response({"message": "Token is missing"}, 401)

                try:
                    # Decode the token and verify the payload
                    payload = jwt.decode(
                        token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
                    )

                    # Check admin requirements
                    if adminRequired:
                        if not payload["admin"]:
                            return make_response(
                                {
                                    "message": "You do not have permission to access this resource"
                                },
                                403,
                            )
                    else:
                        # Check if the user in the token matches the requested user
                        if payload["id"] != kwargs["id"]:
                            return make_response(
                                {
                                    "message": "You do not have permission to access this resource"
                                },
                                403,
                            )

                except (DecodeError, ExpiredSignatureError):
                    return make_response({"message": "Invalid or expired token"}, 401)

                # Call the decorated function if all checks pass
                return f(*args, **kwargs)

            except Exception as e:
                print(e)
                return make_response({"message": "Internal server error"}, 500)

        return decorated_function

    return decorator
