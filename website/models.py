from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Offers(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images')
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name