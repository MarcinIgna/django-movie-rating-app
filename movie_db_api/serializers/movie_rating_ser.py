# from rest_framework import serializers
# from movie_db_api.models.movie_rating import MovieRating
# from movie_db_api.serializers.rating import RatingSerializer



# class MovieRatingSerializer(serializers.ModelSerializer):
#     user_ratings = RatingSerializer(many=True)
#     number_of_ratings = serializers.SerializerMethodField()

#     class Meta:
#         model = MovieRating
#         fields = ['user_ratings', 'number_of_ratings']

#     def get_number_of_ratings(self, obj):
#         ratings = obj.user_ratings
#         number_of_ratings = len(ratings)
#         rating = sum([rating.value for rating in ratings]) / number_of_ratings if number_of_ratings > 0 else 0
#         return rating










# class MovieRatingSerializer(serializers.ModelSerializer):
#     user_ratings = RatingSerializer(many=True)
#     class Meta:
#         model = MovieRating
#         fields = '__all__'
#     @classmethod
#     def calculate_rating():
#         ratings = self.user_ratings
#         number_of_ratings = len(ratings)
#         raiting = sum([rating.value for rating in ratings])/number_of_ratings
#         return raiting
    
#     number_of_ratings = calculate_rating()
    

    
    
    
    