from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Sai tài khoản")

    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("/users/login/")


def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        # Username đã tồn tại
        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists."
            )

            return redirect("/users/register/")

        # Kiểm tra password
        try:

            validate_password(password)

        except ValidationError as e:

            for error in e.messages:

                messages.error(
                    request,
                    error
                )

            return redirect("/users/register/")

        # Tạo user
        user = User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(
            request,
            "Register successfully."
        )

        return redirect("/users/login/")

    return render(
        request,
        "users/register.html"
    )


@login_required
def my_profile(request):

    profile = request.user.userprofile

    return render(
        request,
        "users/my_profile.html",
        {
            "profile": profile
        }
    )
    
    
@login_required
def edit_profile(request):

    profile = request.user.userprofile

    if request.method == "POST":

        request.user.email = request.POST.get("email")

        profile.phone = request.POST.get("phone")

        profile.address = request.POST.get("address")

        profile.education = request.POST.get("education")

        profile.experience = request.POST.get("experience")

        request.user.save()

        profile.save()

        messages.success(
            request,
            "Profile updated successfully."
        )

        return redirect("/users/profile/")

    return render(
        request,
        "users/edit_profile.html",
        {
            "profile": profile
        }
    )