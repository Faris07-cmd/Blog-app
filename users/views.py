from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import UserRegister


def register(request):
    if request.method == "POST":
        form = UserRegister(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("login")
    else:
        form = UserRegister()

    return render(request, "users/register.html", {"form": form})
