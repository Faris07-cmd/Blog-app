from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView

from .forms import PostForm
from .models import Post


def about(request):
    return render(request, "blog/about.html")


def post_form(request):
    form = PostForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        Post.auhtor = request.user
        form.save()

        messages.success(request, "Posted")
        return redirect("blog-home")
    return render(request, "blog/post.html", {"form": form})


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
