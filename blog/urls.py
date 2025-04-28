# blog/urls.py
from django.urls import path
from core.views import BlogListView, BlogDetailView


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<slug:post_slug>/', BlogDetailView.as_view(), name='blog_detail'),
]