from rest_framework import serializers
from .models import Favorite


class FavSerialzer(serializers.ModelSerializer):
    class Meta:
        fields = ['title', 'author', 'updated', 'timestamp', 'description','played']
        model = Favorite