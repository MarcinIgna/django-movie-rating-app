from movie_db_api.serializers.user import UserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from django.db.models.query import QuerySet




    
class UserViewSet(APIView):
    authentication_classes = [TokenAuthentication]
    
    def get(self, request, pk=None):
        if request.user.is_authenticated and request.user.is_superuser:
            # If the requesting user is a superuser and authenticated, return the user data for all users
            try:
                if pk is not None:
                    user = User.objects.get(pk=pk)
                else:
                    user = User.objects.all()
                serializer = UserSerializer(user, many=isinstance(user, QuerySet))
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)
        elif pk is None and request.user.is_authenticated:
            # If no pk is specified and authenticated, return the current user's data
            user = request.user
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            # If the requesting user is not a superuser and no pk is specified, return a 400 Bad Request response
            return Response("You are not authorized to view this page", status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        # Create a new user
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Create a token for the user
            token, created = Token.objects.get_or_create(user=user)
            
            response_data = {
                "user": serializer.data,
                "token": token.key
            }
            
            return Response(response_data, status=status.HTTP_201_CREATED)
            # Return a valid Response object with status code 201 (Created)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        if pk is None:
            # If no pk is specified, update the current user's data
            user = request.user
        else:
            # If a pk is specified, update the user data for the specified pk
            if pk is not None and request.user.is_authenticated and request.user.is_superuser:
                try:
                    user = User.objects.get(pk=pk)
                    serializer = UserSerializer(user, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    return Response(serializer.errors)
                except User.DoesNotExist:
                    return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)
            
        # If the requesting user is not a superuser and is not the owner of the account, return a 400 Bad Request response
        return Response("You are not authorized to update this account", status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk=None):
        if pk is None:
            # If no pk is specified, delete the current user's account
            user = request.user
            user.delete()
            return Response("User deleted")
        else:
            # If a pk is specified, delete the user account for the specified pk
            if pk is not None and request.user.is_authenticated and request.user.is_superuser:
                try:    
                    user = User.objects.get(pk=pk)
                    user.delete()
                    return Response("User deleted")
                except User.DoesNotExist:
                    return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)
        return Response("You are not authorized to delete this account", status=status.HTTP_400_BAD_REQUEST)
        
    
    
    
    
    
    
# class UserViewSet(APIView):
#     def get(self, request, pk=None):
#         if pk is not None:
#             user = User.objects.get(pk=pk)
#             serializer = UserSerializer(user)
#             return Response(serializer.data)
#         else:
#             users = User.objects.all()
#             serializer = UserSerializer(users, many=True)
#             return Response(serializer.data)
    
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
            
#             # Create a token for the user
#             token, created = Token.objects.get_or_create(user=user)
            
#             response_data = {
#                 "user": serializer.data,
#                 "token": token.key
#             }
            
#             return Response(response_data)
#         return Response(serializer.errors)
    
#     def put(self, request, pk):
#         user = User.objects.get(pk=pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     def delete(self, request, pk):
#         user = User.objects.get(pk=pk)
#         user.delete()
#         return Response("User deleted")
