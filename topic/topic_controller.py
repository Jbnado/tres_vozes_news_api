import datetime
from flask import Blueprint, request, make_response, current_app
from topic.topic_model import TopicModel
from middleware_is_admin import isAdmin

topic_blueprint = Blueprint("topic", __name__)


class TopicController:
    @topic_blueprint.post("/")
    @isAdmin(adminRequired=True)
    def createTopic():
        data = request.get_json()

        try:
            topic = TopicModel(**data)
            topic.saveTopic()
            return topic.json(), 201
        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500

    @topic_blueprint.get("/<id>")
    @isAdmin(adminRequired=True)
    def getOneTopic(id):
        try:
            topic = TopicModel.getOneTopic(id)
            if topic:
                return topic.json(), 200
            return {"message": "Topic not found"}, 404
        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500

    @topic_blueprint.get("/")
    @isAdmin(adminRequired=True)
    def getAllTopics():
        try:
            topics = TopicModel.getAllTopics()
            return [topic.json() for topic in topics], 200
        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500

    @topic_blueprint.patch("/<id>")
    @isAdmin(adminRequired=True)
    def updateTopicById(id):
        try:
            data = request.get_json()
            topic = TopicModel.getOneTopic(id)
            if topic:
                topic.updateTopic(data["topic"])
                return topic.json(), 200
            return {"message": "Topic not found"}, 404
        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500

    @topic_blueprint.delete("/<id>")
    @isAdmin(adminRequired=True)
    def delete(id):
        try:
            topic = TopicModel.getOneTopic(id)
            if topic:
                topic.deleteTopic()
                return {"message": "Topic deleted successfully!"}, 200
            return {"message": "Topic not found"}, 404
        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500
