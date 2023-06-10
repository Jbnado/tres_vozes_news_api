import uuid
from sqlalchemy.dialects.postgresql import UUID
import datetime
from db import db


class LikedModel(db.Model):
    __tablename__ = "LikedNews"

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Users.id"), nullable=False)
    news_id = db.Column(UUID(as_uuid=True), db.ForeignKey("News.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.datetime.now(),
        nullable=False,
        onupdate=datetime.datetime.now(),
    )

    def __init__(self, user_id, news_id):
        self.user_id = user_id
        self.news_id = news_id

    def saveLiked(self):
        db.session.add(self)
        db.session.commit()

    def deleteLiked(self):
        db.session.delete(self)
        db.session.commit()
