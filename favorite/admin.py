from django.contrib import admin
from .models import Favorite


@admin.register(Favorite)
class FavAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'updated', 'author', 'played']