from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    view_count = models.IntegerField(default=0)
    # published = models.booleanField()


# class Comment(models.Model):
