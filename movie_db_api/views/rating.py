from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.exceptions import PermissionDenied


from movie_db_api.serializers.rating import RatingSerializer
from movie_db_api.models.rating import Rating



class RatingViewSet(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
            # get rating by id or get all ratings
            if request.user.is_superuser:
                try:
                    if pk is not None:
                        rating = Rating.objects.get(pk=pk)
                        serializer = RatingSerializer(rating)
                        return Response(serializer.data)
                    else:
                        ratings = Rating.objects.all()
                        serializer = RatingSerializer(ratings, many=True)
                        return Response(serializer.data)
                except Rating.DoesNotExist:
                    return Response("Rating not found", status=status.HTTP_404_NOT_FOUND)
            else:
                return Response("You are not authorized to view this page", status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        # Add a new rating for the authenticated user
        movie_id = request.data.get('movie')  # Retrieve the movie_id from the request data
        serializer = RatingSerializer(data=request.data, context={'request': request, 'movie_id': movie_id})  # Pass the context here
        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk):
        # Update a rating for the authenticated user
        rating = Rating.objects.get(pk=pk)
        print("rating user: ",rating.user)
        print("req user: ",request.user)
        if rating.user != request.user:
            raise PermissionDenied("You are not authorized to edit this rating.")  # Raise an exception if the user does not own the rating
        serializer = RatingSerializer(rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        # Delete a rating for the authenticated user
        try:
            rating = Rating.objects.get(pk=pk)
            if rating.user != request.user:
                raise PermissionDenied("You are not authorized to delete this rating.")  # Raise an exception if the user does not own the rating
            rating.delete()
            return Response("Rating deleted")
        except Rating.DoesNotExist:
            return Response("Rating not found", status=status.HTTP_404_NOT_FOUND)













# class RatingViewSet(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self, request, pk=None):
#         # get rating by id or get all ratings
#         if request.user.is_superuser:
#             if pk is not None:
#                 rating = Rating.objects.get(pk=pk)
#                 serializer = RatingSerializer(rating)
#                 return Response(serializer.data)
#             else:
#                 ratings = Rating.objects.all()
#                 serializer = RatingSerializer(ratings, many=True)
#                 return Response(serializer.data)
#         else:
#             return Response("You are not authorized to view this page", status=status.HTTP_400_BAD_REQUEST)
    
#     def post(self, request):
#         # add a new rating
#         serializer = RatingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     def put(self, request, pk):
#         # update a rating
#         rating = Rating.objects.get(pk=pk)
#         serializer = RatingSerializer(rating, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     def delete(self, request, pk):
#         # delete a rating
#         rating = Rating.objects.get(pk=pk)
#         rating.delete()
#         return Response("Rating deleted")