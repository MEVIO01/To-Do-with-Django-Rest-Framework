from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api_overview"),
    path('task-list/', views.tasks_view, name="tasks_view"),
    path('task-detail/<str:pk>/', views.tasks_detail, name="tasks_detail"),
]