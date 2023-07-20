from django.db import models
from .genre import Genre


class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre)
    description = models.TextField()
    relase_year = models.DateField()

    def __str__(self) -> str:
        return self.title

    
