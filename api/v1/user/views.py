from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth  import login, logout, authenticate

from .serializer import (
    UserSerializer,
    UserUpdateSerializer
)
from .models import User

class UserApi(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserEditApi(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()


class LoginApi(APIView):
    def get(self, request, *args, **kwargs):
        data = request.data
        phone = data.get("phone")
        password = data.get("password")
        user = authenticate(request, phone = phone, password = password)
        if not user:
            return Response({
                "message": "User not found"
            })
        login(request,user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "message": "Successful",
            "token_key": token.key
        }, status=status.HTTP_200_OK)
    
class LogoutApi(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request,*args, **kwargs):
        request.user.auth_token.delete()
        logout(request)
        return Response({
            "message": "User logout"
        }, status=status.HTTP_204_NO_CONTENT)