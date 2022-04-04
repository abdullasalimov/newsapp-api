from django.db import models
from django.contrib.auth.models import User


class Region(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
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


# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     news = models.ForeignKey(News, on_delete=models.CASCADE)
#     value = models.CharField(max_length=10)


class Review(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return self.title
