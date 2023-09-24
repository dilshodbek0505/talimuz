from django.urls import path

from .views import (
    SchoolApi,
    SchoolRUDApi,
    SchoolImageApi,
    SchoolRUDImageApi
)

urlpatterns = [
    path("school/",SchoolApi.as_view()),
    path("school/details/<int:pk>/", SchoolRUDApi.as_view()),
    path("school/image/", SchoolImageApi.as_view()),
    path("school/image/details/<int:pk>/", SchoolRUDImageApi.as_view())
]
