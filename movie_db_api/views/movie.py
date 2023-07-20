from movie_db_api.serializers.movie import MovieSerializer
from movie_db_api.models.movie import Movie
from rest_framework.views import APIView
from rest_framework.response import Response

class MovieViewSet(APIView):
    def get(self, request, pk=None):
        # get movie by id or get all movies
        if pk is not None:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        else:
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        # add a new movie
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self, request, pk):
        # update a movie
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        # delete a movie
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response("Movie deleted")