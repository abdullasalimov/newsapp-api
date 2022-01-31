from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("collections", views.CollectionViewSet, basename="collections")

collection_router = routers.NestedDefaultRouter(
    router, "collections", lookup="collection"
)
collection_router.register("topics", views.TopicViewSet, basename="topics")

topics_router = routers.NestedDefaultRouter(collection_router, "topics", lookup="topic")
topics_router.register("news", views.NewsViewSet, basename="news")

news_router = routers.NestedDefaultRouter(topics_router, "news", lookup="new")
news_router.register("reviews", views.ReviewViewSet, basename="new-reviews")


urlpatterns = [
    path("", include(router.urls)),
    path("", include(collection_router.urls)),
    path("", include(topics_router.urls)),
    path("", include(news_router.urls)),
]
