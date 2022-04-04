from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("regions", views.RegionViewSet, basename="regions")

region_router = routers.NestedDefaultRouter(router, "regions", lookup="region")
region_router.register("categories", views.CategoryViewSet, basename="categories")

categories_router = routers.NestedDefaultRouter(
    region_router, "categories", lookup="category"
)
categories_router.register("news", views.NewsViewSet, basename="news")

news_router = routers.NestedDefaultRouter(categories_router, "news", lookup="news")
news_router.register("reviews", views.ReviewViewSet, basename="new-reviews")


urlpatterns = [
    path("", include(router.urls)),
    path("", include(region_router.urls)),
    path("", include(categories_router.urls)),
    path("", include(news_router.urls)),
]
