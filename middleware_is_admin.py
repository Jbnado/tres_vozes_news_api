# Criar um middleware que verifica se o usuário é admin a partir do token armazenado nos cookies.
import jwt
from flask import request, make_response, current_app
from functools import wraps


def isAdmin(adminRequired=True):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                # get token from header authorization
                token = request.headers.get("Authorization")
                if not token:
                    return make_response({"message": "Token is missing"}, 401)
                payload = jwt.decode(
                    token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
                )
                # Caso não seja necessário ser admin:
                if adminRequired == False:
                    # Checar se o usuário que está fazendo a requisição é o mesmo que está no token
                    if payload["id"] != kwargs["id"]:
                        return make_response(
                            {
                                "message": "You do not have permission to access this resource"
                            },
                            403,
                        )
                    # Se não for o mesmo, checar se é admin ou não
                    elif payload["admin"] == True:
                        return f(*args, **kwargs)

                # Caso seja necessário ser admin:
                elif adminRequired == True:
                    if payload["admin"] == adminRequired:
                        return f(*args, **kwargs)
                    return make_response(
                        {
                            "message": "You do not have permission to access this resource"
                        },
                        403,
                    )
            except Exception as e:
                print(e)
                return {"message": "Internal server error"}, 500

        return decorated_function

    return decorator
