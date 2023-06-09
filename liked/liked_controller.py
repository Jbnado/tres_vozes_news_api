from flask import Blueprint, request
from liked.liked_model import LikedModel

liked_blueprint = Blueprint("liked", __name__)


class LikedController:
    @liked_blueprint.post("/")
    def createLiked():
        data = request.get_json()

        try:
            liked = LikedModel(**data)
            liked.saveLiked()
            return liked.json(), 201
        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500

    @liked_blueprint.delete("/<id>")
    def delete(id):
        try:
            liked = LikedModel.getOneLiked(id)
            if liked:
                liked.deleteLiked()
                return {"message": "Liked deleted"}, 200
            return {"message": "Liked not found"}, 404
        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500
