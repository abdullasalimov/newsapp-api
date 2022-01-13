from django.db import models


class Language(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        def __str__(self) -> str:
            return self.title


class Topic(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        def __str__(self) -> str:
            return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_favourite = models.BooleanField(default=False)
    #seen_count
    #like_count

    class Meta:
        def __str__(self) -> str:
            return self.title


class Comment(models.Model):
    pass

