import base64
import json
import os
import bcrypt
import jwt
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from tres_vozes_news_api.models.user import User
from tres_vozes_news_api.serializers import UserSerializer

load_dotenv()


def encrypt_password(password):
    saltRounds = 10
    return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt(saltRounds))


def decrypt_password(password, hashed):
    password_bytes = password.encode('utf8')
    return bcrypt.checkpw(password_bytes, hashed)


@ csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        data['password'] = encrypt_password(data['password'])
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User was deleted successfully!'}, status=204)


@ csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = User.objects.get(email=data['email'])
            print(data['password'], user.password)
        except User.DoesNotExist:
            return JsonResponse({'message': 'The user does not exist'}, status=404)
        if user.password == decrypt_password(data['password'], user.password):
            payload = {
                'id': str(user.id),
                'admin': user.admin,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
            }
            token = jwt.encode(payload, os.getenv(
                'SECRET_KEY'), algorithm='HS256')
            token = token.decode('utf8')
            response = JsonResponse({
                'message': 'User logged in successfully!',
                'token': token,
                'name': user.name,
            })
            response.set_cookie('token', token)
            return response
        return JsonResponse({'message': 'Invalid password'}, status=400)
