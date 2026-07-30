from django.urls import path
from .views import (
    UserLoginView,
    register,
    profile,
    edit_profile,
    user_logout,
)

urlpatterns = [

    path("register/", register, name="register"),

    path(
        "login/",
        UserLoginView.as_view(),
        name="login",
    ),

    path("logout/", user_logout, name="logout"),

    path("profile/", profile, name="profile"),

    path(
        "profile/edit/",
        edit_profile,
        name="edit_profile",
    ),
]