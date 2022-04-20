from django.utils import timezone
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import News, Region, Category, Review
from .serializers import (
    RegionSerializer,
    CategorySerializer,
    NewsSerializer,
    ReviewSerializer,
)


class RegionViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def get_serializer_context(self):
        return {"request": self.request}


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(region_id=self.kwargs["region_pk"])

    def get_serializer_context(self):
        return {"region_id": self.kwargs["region_pk"]}


class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def list(self, request, *args, **kwargs):
        # call the original 'list' to get the original response.
        response_data = super(NewsViewSet, self).list(request, *args, **kwargs)

        data = {
            "status": 0,
            "message": "Success",
            "data": {
                "updatedAt": News.objects.order_by("-created_at")
                .first()
                .created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "serverTime": timezone.now().strftime("%Y-%m-%d %H:%M:%S"),
                "news": [
                    {
                        "id": obj["id"],
                        "title": obj["title"],
                        "created_at": obj["created_at"],
                        "description": obj["description"],
                        "category": obj["category"],
                        "region": obj["region"],
                        "is_favourite": obj["is_favourite"],
                        "author": obj["author"],
                        "views": obj["views"],
                        "likes": obj["total_likes"],
                    }
                    for obj in response_data.data
                ],
            },
        }

        return Response(data)

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs["category_pk"])

    def get_serializer_context(self):
        return {"category_id": self.kwargs["category_pk"]}

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.views = obj.views + 1
        obj.save(update_fields=("views",))
        return super().retrieve(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(news_id=self.kwargs["news_pk"])

    def get_serializer_context(self):
        return {"news_id": self.kwargs["news_pk"]}
