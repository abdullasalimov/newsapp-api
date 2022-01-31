from django.contrib import admin
from .models import Article, Topic, Collection, Review

admin.site.register(Collection)
admin.site.register(Topic)
admin.site.register(Article)
admin.site.register(Review)
