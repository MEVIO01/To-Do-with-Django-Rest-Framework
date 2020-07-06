from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api_overview"),
    path('task-list/', views.tasks_view, name="tasks_view"),
    path('task-detail/<str:pk>/', views.tasks_detail, name="tasks_detail"),
    path('task-create/', views.tasks_create, name="tasks_create"),
    path('task-update/<str:pk>/', views.tasks_update, name="tasks_update"),
    path('task-delete/<str:pk>/', views.tasks_delete, name="tasks_delete"),
]