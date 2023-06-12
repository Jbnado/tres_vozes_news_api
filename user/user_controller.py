import datetime
import jwt
from flask import Blueprint, request, make_response, current_app
from user.user_model import UserModel
from middleware_is_admin import isAdmin

user_blueprint = Blueprint("user", __name__)


class UserController:
    @user_blueprint.get("/<id>")
    @isAdmin(adminRequired=True)
    def getUserById(id):
        try:
            user = UserModel.getOneUser(id)
            if user:
                return user.json(), 200
            return {"message": "User not found"}, 404
        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500

    @user_blueprint.patch("/<id>")
    @isAdmin(adminRequired=False)
    def updateUserById(id):
        try:
            data = request.get_json()
            user = UserModel.getOneUser(id)
            if user:
                user.updateUser(data)
                return user.json(), 200
            return {"message": "User not found"}, 404
        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500

    @user_blueprint.delete("/<id>")
    @isAdmin(adminRequired=True)
    def delete(id):
        try:
            user = UserModel.getOneUser(id)
            if user:
                user.deleteUser()
                return {"message": "User deleted successfully!"}, 200
            return {"message": "User not found"}, 404
        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500

    @user_blueprint.get("/")
    @isAdmin(adminRequired=True)
    def getAllUsers():
        try:
            users = UserModel.getAllUsers()
            return [user.json() for user in users], 200
        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500

    @user_blueprint.post("/")
    def post():
        data = request.get_json()
        if UserModel.getUserByEmail(data["email"]):
            return {"message": "Email already registered"}, 400

        try:
            user = UserModel(**data)
            user.saveUser()
            return user.json(), 201
        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500

    @user_blueprint.post("/login")
    def login():
        token = request.cookies.get("token")
        if token:
            return {"message": "User already logged in"}, 400

        data = request.get_json()
        email = data["email"]
        password = data["password"]

        try:
            user = UserModel.login(email, password)
        except Exception as e:
            print(e)
            return {"message": "User not found"}, 404

        if user == None:
            return {"message": "Invalid credentials"}, 401
        else:
            payload = {
                "id": user["id"],
                "admin": user["admin"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=3),
            }
            token = jwt.encode(
                payload,
                current_app.config["SECRET_KEY"],
                algorithm="HS256",
            )
            return make_response(
                {"message": "User logged in successfully!", "token": token}, 200
            )

    @user_blueprint.post("/logout")
    def logout():
        token = request.cookies.get("token")
        if not token:
            return {"message": "User not logged in"}, 400
        response = make_response({"message": "User logged out successfully!"}, 200)
        response.set_cookie("token", "", expires=0)
        return response
