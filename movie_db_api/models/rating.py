from django.db import models
from django.contrib.auth.models import User
from .movie import Movie


class Rating(models.Model):
    value = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, related_name='movie_ratings')

    def __str__(self):
        return f"Rating: {self.value} | User: {self.user.username} | Movie: {self.movie.title}"