from django.contrib import admin
from .models import News, Category, Region, Review

admin.site.register(Region)
admin.site.register(Category)
admin.site.register(News)
admin.site.register(Review)
