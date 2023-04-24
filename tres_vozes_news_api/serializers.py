from rest_framework import serializers
from .models.user import User
from .models.topic import Topic
from .models.news import News
from .models.liked_news import LikedNews


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class LikedNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedNews
        fields = '__all__'
