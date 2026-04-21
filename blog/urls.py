from django.urls import path

from .views import PostListView, about

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("about/", about, name="blog-about"),
]
