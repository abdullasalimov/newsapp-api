from django.urls import path
from . import views

urlpatterns = [
    path("news/", views.news_list),
    path("news/<int:id>/", views.news_detail),
]
