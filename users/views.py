from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer, UserLoginSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
import jwt

class UserSignupView(APIView):

    def post(self, request):
        userserializer = UserSerializer(data=request.data)
        userserializer.is_valid(raise_exception=True)
        userserializer.save()
        user = authenticate(request,
            username=userserializer.data.get('username'),
            password=request.data.get('password')
        )
        if user is not None:
            token = RefreshToken.for_user(user)
            data = {
                'refresh' : str(token),
                'access' : str(token.access_token),
                'user' : {
                    'pk' : user.id,
                    'username' : user.username,
                    'email' : user.email,
                }
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UserSigninAPIView(APIView):

    def post(self, request):
        login = UserLoginSerializer(data=request.data)
        login.is_valid(raise_exception=True)
        return Response(login.validated_data)

class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            refresh_token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        try:
            user_id = request.auth.get('user_id')
            user = User.objects.get(id=user_id)
            if user:
                user.delete()
        except ValidationError as v:
            print("validation error", v)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated,]

    def get_user_obj(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_user_obj(pk)
        if user.is_superuser or user.id == request.user.id:
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user_id = request.auth.get('user_id')
            user = User.objects.get(id=user_id)
            user_obj = self.get_user_obj(pk)
            if user and user.id == user_obj.id:
                user.delete()
        except ValidationError as v:
            print("validation error", v)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        '''Update single object of Application'''
        user_obj = self.get_user_obj(pk)
        user_id = request.auth.get('user_id')
        user = User.objects.get(id=user_id)
        if user and user.id == user_obj.id:
            user_serializer = UserSerializer(user_obj, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data)
        return Response(user_serializer.errors ,status.HTTP_400_BAD_REQUEST)
