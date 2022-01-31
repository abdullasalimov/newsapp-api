from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register("news", views.NewsViewSet)
router.register("collections", views.CollectionViewSet)
router.register("topics", views.TopicViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
