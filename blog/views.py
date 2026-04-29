from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from .forms import PostForm
from .models import Post


class About(TemplateView):
    template_name = "blog/about.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post.html"
    success_url = reverse_lazy("blog-home")
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        form.instance.auhtor = self.request.user
        messages.success(self.request, "Posted")
        return super().form_valid(form)


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
