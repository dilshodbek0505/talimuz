from django.urls import path

from .views import (
    UserApi,
    LoginApi,
    LogoutApi,
    UserEditApi
)

urlpatterns = [
    path("", UserApi.as_view()),
    path("login/", LoginApi.as_view()),
    path("logout/", LogoutApi.as_view()),
    path("details/<int:pk>/", UserEditApi.as_view())
]
