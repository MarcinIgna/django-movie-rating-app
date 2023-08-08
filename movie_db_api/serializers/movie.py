from rest_framework import serializers
from movie_db_api.models.movie import Movie
from movie_db_api.models.genre import Genre
from movie_db_api.serializers.genre import GenreSerializer
from movie_db_api.serializers.rating import RatingSerializer
from movie_db_api.models.rating import Rating

# from movie_db_api.serializers.movie_rating_ser import MovieRatingSerializer

class MovieSerializer(serializers.ModelSerializer):

    genre = GenreSerializer(many=True)
    movie_ratings = RatingSerializer(many=True, required=False)
    number_of_ratings = serializers.SerializerMethodField()
    
    # get the average rating for the movie
    def get_number_of_ratings(self, obj):
        ratings = Rating.objects.filter(movie_id=obj.id)
        print(ratings)
        
        
        len_ratings = len(ratings)
        rating = sum([rating.value for rating in ratings]) / len_ratings if len_ratings > 0 else 0
        return rating

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'description', 'relase_year', "movie_ratings","number_of_ratings"]

    def create(self, validated_data):
        genre_data = validated_data.pop('genre', [])
        raiting_data = validated_data.pop('rating')
        movie = super().create(validated_data)
        
        
        for genre in genre_data:
            genre_obj, _ = Genre.objects.get_or_create(name=genre['name'])
            movie.genre.add(genre_obj)
        return movie

    def update(self, instance, validated_data):
        genre_data = validated_data.pop('genre', [])
        instance = super().update(instance, validated_data)
        instance.genre.clear()
        for genre in genre_data:
            genre_obj, _ = Genre.objects.get_or_create(name=genre['name'])
            instance.genre.add(genre_obj)
        return instance
