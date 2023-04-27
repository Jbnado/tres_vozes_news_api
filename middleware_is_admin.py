# Criar um middleware que verifica se o usuário é admin a partir do token armazenado nos cookies.
import jwt
from flask import request, make_response, current_app
from functools import wraps


def isAdmin(adminRequired=True):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                token = request.cookies.get('token')
                if not token:
                    return make_response({'message': 'Token is missing'}, 401)
                payload = jwt.decode(
                    token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
                if payload['admin'] == adminRequired:
                    return f(*args, **kwargs)
                return make_response({'message': 'You do not have permission to access this resource'}, 403)
            except Exception as e:
                print(e)
                return {'message': 'Internal server error'}, 500
        return decorated_function
    return decorator
