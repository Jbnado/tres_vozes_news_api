from flask import Blueprint, request
from news.news_model import NewsModel
from middleware_is_admin import isAdmin

news_blueprint = Blueprint("news", __name__)


class NewsController:
    @news_blueprint.post("/")
    @isAdmin(adminRequired=True)
    def createNews():
        data = request.get_json()

        try:
            news = NewsModel(**data)
            news.saveNews()
            return news.json(), 201
        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500

    @news_blueprint.get("/<id>")
    @isAdmin(adminRequired=True)
    def getOneNews(id):
        try:
            news = NewsModel.getOneNews(id)
            if news:
                return news.json(), 200
            return {"message": "News not found"}, 404
        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500

    @news_blueprint.get("/")
    @isAdmin(adminRequired=True)
    def getAllNews():
        try:
            news = NewsModel.getAllNews()
            return [news.json() for news in news], 200
        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500

    @news_blueprint.patch("/<id>")
    @isAdmin(adminRequired=True)
    def updateNewsById(id):
        try:
            data = request.get_json()
            news = NewsModel.getOneNews(id)
            if news:
                news.updateNews(data)
                return news.json(), 200
            return {"message": "News not found"}, 404
        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500

    @news_blueprint.delete("/<id>")
    @isAdmin(adminRequired=True)
    def delete(id):
        try:
            news = NewsModel.getOneNews(id)
            if news:
                news.deleteNews()
                return {"message": "News deleted"}, 200
            return {"message": "News not found"}, 404
        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500
