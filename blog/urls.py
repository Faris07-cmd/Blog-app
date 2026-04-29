from django.urls import path

from .views import About, PostCreateView, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("about/", About.as_view(), name="blog-about"),
    path("post/", PostCreateView.as_view(), name="post"),
]
