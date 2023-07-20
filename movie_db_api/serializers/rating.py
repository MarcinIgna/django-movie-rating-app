from rest_framework import serializers
from movie_db_api.models.rating import Rating


class RatingSerializer(serializers.ModelSerializer):
    movie = serializers.SlugRelatedField(slug_field='title', read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    

    class Meta:
        model = Rating
        fields = ('id', 'user', 'value', 'movie')
        
    def create(self, validated_data):
        user = self.context['request'].user
        rating = Rating.objects.create(user=user, **validated_data)
        movie_id = self.context['view'].kwargs['movie_id']
        # MovieRating.objects.create(movie_id=movie_id, rating=rating)
        return rating
    
    def update(self, instance, validated_data):
        instance.value = validated_data.get('value', instance.value)
        instance.save()
        return instance