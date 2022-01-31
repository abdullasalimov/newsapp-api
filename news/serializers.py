from dataclasses import fields
from rest_framework import serializers
from .models import Article, Collection, Review, Topic


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title", "slug"]


class TopicSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        "collection_pk": "collection_pk",
    }

    class Meta:
        model = Topic
        fields = ["id", "title"]
        collection = CollectionSerializer()

    def create(self, validated_data):
        collection_id = self.context["collection_id"]
        return Topic.objects.create(collection_id=collection_id, **validated_data)


class ArticleSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        "collection_pk": "collection_pk",
        "topic_pk": "topic_pk",
    }

    class Meta:
        model = Article
        fields = [
            "id",
            "collection",
            "topic",
            "title",
            "description",
            "created_at",
            "views",
            "likes",
            "is_favourite",
        ]

    def create(self, validated_data):
        topic_id = self.context["topic_id"]
        return Article.objects.create(topic_id=topic_id, **validated_data)


class ReviewSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        "collection_pk": "collection_pk",
        "topic_pk": "topic_pk",
        "new_pk": "new_pk",
    }

    class Meta:
        model = Review
        fields = ["id", "date", "name", "description"]

    def create(self, validated_data):
        new_id = self.context["new_id"]
        return Review.objects.create(new_id=new_id, **validated_data)
