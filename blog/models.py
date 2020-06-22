from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)

    def published(self):
        self.published = timezone.now()
        self.save()

    @classmethod
    def get_objects(cls):
        cls.objects.create(title='title')
        
