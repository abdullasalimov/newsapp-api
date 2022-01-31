from django.db import models
from django.contrib.auth.models import User


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
    likes = models.ManyToManyField(User, blank=True, default=None, related_name="likes")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    views = models.IntegerField(default=0, null=True, blank=True)

    @property
    def number_of_likes(self):
        return self.likes.all().count()

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    value = models.CharField(max_length=10)


class Review(models.Model):
    new = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
