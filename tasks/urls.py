
from django.urls import path
from . import views

urlpatterns = [
    path('accounts/logout/', views.logout_view, name='logout'),
    path('login/', views.login, name='login'),
    path('', views.tasks_list, name='tasks_list_view'),
    path('tasks/<str:status>/', views.tasks_list, name='filtered_tasks_list'),
    path('edit/<int:id>/', views.editTask, name="edit-task"),
    path('create_task/', views.create_task, name='create_task'),
    path('tasks/delete/<int:id>/', views.delete_task, name='delete_task'),
]