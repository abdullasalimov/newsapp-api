from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("news", views.NewsViewSet)
router.register("collections", views.CollectionViewSet)
router.register("topics", views.TopicViewSet)

news_router = routers.NestedDefaultRouter(router, "news", lookup="new")
news_router.register("reviews", views.ReviewViewSet, basename="new-reviews")

urlpatterns = [
    path("", include(router.urls)),
] + news_router.urls
