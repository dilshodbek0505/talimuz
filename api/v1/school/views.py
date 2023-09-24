from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)


from .serializer import (
    SchoolImageSerializer,
    SchoolSerializer
)
from .models import (
    School,
    SchoolImage
)

class SchoolApi(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = SchoolSerializer
    queryset = School.objects.select_related("user").all()

class SchoolImageApi(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = SchoolImageSerializer
    queryset = SchoolImage.objects.select_related("school").all()

class SchoolRUDApi(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = SchoolSerializer
    queryset = School.objects.select_related("user").all()

class SchoolRUDImageApi(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = SchoolImageSerializer
    queryset = SchoolImage.objects.select_related("school").all()
