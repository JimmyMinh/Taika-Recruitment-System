from django.urls import path
from .views import (
    login_view,
    logout_view,
    register_view,
    my_profile, edit_profile
)

urlpatterns = [
    path(
        "login/",
        login_view,
        name="login"
    ),

    path(
        "logout/",
        logout_view,
        name="logout"
    ),

    path(
        "register/",
        register_view,
        name="register"
    ),

    path(
        "profile/",
        my_profile,
        name="my-profile"
    ),

    path(
        "profile/edit/",
        edit_profile,
        name="edit-profile"
    ),
]