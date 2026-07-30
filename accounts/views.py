from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render

from .forms import UserRegistrationForm, UserUpdateForm


class UserLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        return "/"
def register(request):

    if request.method == "POST":

        form = UserRegistrationForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            messages.success(request, "Registration Successful.")

            return redirect("login")

    else:

        form = UserRegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )
@login_required
def profile(request):

    return render(
        request,
        "accounts/profile.html",
    )
@login_required
def edit_profile(request):

    if request.method == "POST":

        form = UserUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user,
        )

        if form.is_valid():

            form.save()

            messages.success(request, "Profile Updated.")

            return redirect("profile")

    else:

        form = UserUpdateForm(instance=request.user)

    return render(
        request,
        "accounts/edit_profile.html",
        {"form": form},
    )
@login_required
def user_logout(request):

    logout(request)

    return redirect("home")