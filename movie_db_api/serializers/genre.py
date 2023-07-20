from rest_framework import serializers
from movie_db_api.models.genre import Genre




class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]