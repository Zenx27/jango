from django.urls import path
from .views import (
    TaskListView, TaskCreateView, TaskUpdateView,
    TaskDeleteView, complete_task
)

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/add/', TaskCreateView.as_view(), name='task_add'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/<int:pk>/complete/', complete_task, name='task_complete'),
]
