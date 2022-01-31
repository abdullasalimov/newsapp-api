from rest_framework.viewsets import ModelViewSet
from .models import Article, Collection, Topic, Review
from .serializers import (
    ArticleSerializer,
    CollectionSerializer,
    ReviewSerializer,
    TopicSerializer,
)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def get_serializer_context(self):
        return {"request": self.request}


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def get_serializer_context(self):
        return {"request": self.request}


class NewsViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_serializer_context(self):
        return {"request": self.request}


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
