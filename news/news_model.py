import uuid
from sqlalchemy.dialects.postgresql import UUID
import datetime
from db import db


class NewsModel(db.Model):
    __tablename__ = "News"

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer, default=0, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.datetime.now(),
        nullable=False,
        onupdate=datetime.datetime.now(),
    )
    author_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Users.id"), nullable=False)
    topic_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Topics.id"), nullable=False)
    author = db.relationship("UserModel")
    topic = db.relationship("TopicModel")

    def __init__(self, title, content, author_id, topic_id):
        self.title = title
        self.content = content
        self.author_id = author_id
        self.topic_id = topic_id

    def saveNews(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getOneNews(id):
        return NewsModel.query.filter_by(id=id).first()

    @staticmethod
    def getAllNews():
        return NewsModel.query.all()

    def updateNews(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def deleteNews(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "content": self.content,
            "likes": self.likes,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
            "author": self.author.json(),
            "topic": self.topic.json(),
        }
