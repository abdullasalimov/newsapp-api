from rest_framework import serializers
from .models import News, Region, Category, Review


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "title", "slug"]


class CategorySerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        "region_pk": "region_pk",
    }

    class Meta:
        model = Category
        fields = ["id", "title"]
        region = RegionSerializer()

    def create(self, validated_data):
        region_id = self.context["region_id"]
        return Category.objects.create(region_id=region_id, **validated_data)


class NewsSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        "region_pk": "region_pk",
        "category_pk": "category_pk",
    }

    class Meta:
        model = News
        fields = [
            "id",
            "region",
            "category",
            "title",
            "description",
            "created_at",
            "views",
            "is_favourite",
            "author",
        ]

        read_only_fields = ["likes"]

    def to_representation(self, instance):
        return {
            "status": 0,
            "message": "Success",
            "data": {
                "updatedAt": "2020-08-31 17:49:15",
                "serverTime": "2022-03-23 15:10:11",
                "news": [
                    {
                        "id": instance.id,
                        "title": instance.title,
                        "created_at": instance.created_at,
                    }
                ],
            },
        }

    def create(self, validated_data):
        category_id = self.context["category_id"]
        return News.objects.create(category_id=category_id, **validated_data)


class ReviewSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        "region_pk": "region_pk",
        "category_pk": "category_pk",
        "news_pk": "news_pk",
    }

    class Meta:
        model = Review
        fields = ["id", "date", "name", "description"]

    def create(self, validated_data):
        news_id = self.context["news_id"]
        return Review.objects.create(news_id=news_id, **validated_data)
