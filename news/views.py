from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer


@api_view()
def news_list(request):
    queryset = Article.objects.all()
    serializer = ArticleSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def news_detail(request, id):
    article = get_object_or_404(Article, pk=id)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
