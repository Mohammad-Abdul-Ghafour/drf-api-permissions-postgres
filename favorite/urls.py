from django.urls import path
from .views import FavDetail , FavList

urlpatterns = [
    path('', FavList.as_view(), name = 'fav_list'),
    path('<int:pk>/',FavDetail.as_view(), name = 'fav_detail')
]