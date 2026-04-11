from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import PostForm
from .models import Post


def home(request):
    posts = Post.objects.all()

    return render(request, "blog/home.html", {"posts": posts})


def about(request):
    return render(request, "blog/about.html")


def post_form(request):
    form = PostForm(request.POST or None)
    if required.method == "POST" and form.is_valid():
        Post.author = request.user
        form.save()
        message.success(request, "Posted")
        return redirect("blog-home")
    return render(request, "blog/post.html", {"form": form})
