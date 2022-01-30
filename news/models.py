from operator import mod
from django.db import models
from django.contrib.auth.models import User
from django.forms import SlugField


class Collection(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=255)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_favourite = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, blank=True)
    # seen_count

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    pass
