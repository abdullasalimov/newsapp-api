from unicodedata import category
from rest_framework import serializers

from news.models import Collection, Topic


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Topic.objects.all(), source="topic"
    )
    language = serializers.PrimaryKeyRelatedField(
        queryset=Collection.objects.all(), source="collection"
    )
