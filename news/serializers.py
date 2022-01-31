from dataclasses import fields
from rest_framework import serializers
from .models import Article, Collection, Review, Topic


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title", "slug"]


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ["id", "title"]
        collection = CollectionSerializer()


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "description",
            "topic",
            "collection",
            "created_at",
            "is_favourite",
            "likes",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "date", "name", "description", "article"]
