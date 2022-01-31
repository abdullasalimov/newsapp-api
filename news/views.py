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
    serializer_class = TopicSerializer

    def get_queryset(self):
        return Topic.objects.filter(collection_id=self.kwargs["collection_pk"])

    def get_serializer_context(self):
        return {"collection_id": self.kwargs["collection_pk"]}


class NewsViewSet(ModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(topic_id=self.kwargs["topic_pk"])

    def get_serializer_context(self):
        return {"topic_id": self.kwargs["topic_pk"]}

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.views = obj.views + 1
        obj.save(update_fields=("views",))
        return super().retrieve(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(new_id=self.kwargs["new_pk"])

    def get_serializer_context(self):
        return {"new_id": self.kwargs["new_pk"]}
