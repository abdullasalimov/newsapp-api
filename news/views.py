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
