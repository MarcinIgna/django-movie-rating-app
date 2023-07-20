from django.urls import path
from .views.movie import MovieViewSet 
from .views.user import UserViewSet
from .views.rating import RatingViewSet

app_name = "movie_db_api"

urlpatterns = [
    path('movies/', MovieViewSet.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieViewSet.as_view(), name='movie-detail'),
    path('users/', UserViewSet.as_view(), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view(), name='user-detail'),
    path('ratings/', RatingViewSet.as_view(), name='rating-list'),
    path('ratings/<int:pk>/', RatingViewSet.as_view(), name='rating-detail'),
]
