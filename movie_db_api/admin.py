from django.contrib import admin
from .models.genre import Genre
from .models.rating import Rating
from .models.movie import Movie


admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Movie)


