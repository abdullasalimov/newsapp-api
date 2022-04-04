from rest_framework.viewsets import ModelViewSet
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
