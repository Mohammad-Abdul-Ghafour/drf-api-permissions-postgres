from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import FavSerialzer
from .models import Favorite
from .permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user

# CR views
class FavList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Favorite.objects.all()
    serializer_class = FavSerialzer

# RUD view
class FavDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Favorite.objects.all()
    serializer_class = FavSerialzer