import uuid
from sqlalchemy.dialects.postgresql import UUID, DATE
import datetime
from db import db


class TopicModel(db.Model):
    __tablename__ = "Topics"

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    topic = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.datetime.now(),
        nullable=False,
        onupdate=datetime.datetime.now(),
    )

    def __init__(self, topic):
        self.topic = topic

    def saveTopic(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getOneTopic(id):
        return TopicModel.query.filter_by(id=id).first()

    @staticmethod
    def getAllTopics():
        return TopicModel.query.all()

    def updateTopic(self, topic):
        self.topic = topic
        db.session.commit()

    def deleteTopic(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {
            "id": str(self.id),
            "topic": self.topic,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
        }
