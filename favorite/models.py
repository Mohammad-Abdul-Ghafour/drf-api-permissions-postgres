from django.db import models
from django.contrib.auth import get_user_model


class Favorite(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now = False, auto_now_add=True)
    updated = models.DateTimeField(auto_now = True, auto_now_add=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    played = models.BooleanField(default=False)

    def __str__(self):
        return self.title