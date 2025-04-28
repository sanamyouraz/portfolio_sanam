# projects/urls.py
from django.urls import path
from core.views import ProjectListView, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('<slug:project_slug>/', ProjectDetailView.as_view(), name='project_detail'),
]
