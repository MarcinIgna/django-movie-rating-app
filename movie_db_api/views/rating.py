from rest_framework.views import APIView
from rest_framework.response import Response

from movie_db_api.serializers.rating import RatingSerializer
from movie_db_api.models.rating import Rating


class RatingViewSet(APIView):
    def get(self, request, pk=None):
        # get rating by id or get all ratings
        if pk is not None:
            rating = Rating.objects.get(pk=pk)
            serializer = RatingSerializer(rating)
            return Response(serializer.data)
        else:
            ratings = Rating.objects.all()
            serializer = RatingSerializer(ratings, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        # add a new rating
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self, request, pk):
        # update a rating
        rating = Rating.objects.get(pk=pk)
        serializer = RatingSerializer(rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        # delete a rating
        rating = Rating.objects.get(pk=pk)
        rating.delete()
        return Response("Rating deleted")