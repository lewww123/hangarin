"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from tasks import views
from tasks.auth_views import CustomLoginView, CustomLogoutView  # Correct import from app

urlpatterns = [
    path('admin/', admin.site.urls),

    # Allauth URLs (optional if using social login)
    path('accounts/', include('allauth.urls')),

    # Custom Login / Logout
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # Home
    path('', views.HomePageView.as_view(), name='home'),

    # Task URLs
    path('task_list/', views.TaskList.as_view(), name='task-list'),
    path('task_list/add/', views.TaskCreateView.as_view(), name='task-add'),
    path('task_list/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('task_list/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),

    # Priority URLs
    path('priority_list/', views.PriorityList.as_view(), name='priority-list'),
    path('priority_list/add/', views.PriorityCreateView.as_view(), name='priority-add'),
    path('priority_list/<int:pk>/', views.PriorityUpdateView.as_view(), name='priority-update'),
    path('priority_list/<int:pk>/delete/', views.PriorityDeleteView.as_view(), name='priority-delete'),

    # Category URLs
    path('category_list/', views.CategoryList.as_view(), name='category-list'),
    path('category_list/add/', views.CategoryCreateView.as_view(), name='category-add'),
    path('category_list/<int:pk>/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category_list/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),

    # Note URLs
    path('note_list/', views.NoteList.as_view(), name='note-list'),
    path('note_list/add/', views.NoteCreateView.as_view(), name='note-add'),
    path('note_list/<int:pk>/', views.NoteUpdateView.as_view(), name='note-update'),
    path('note_list/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note-delete'),

    # SubTask URLs
    path('subtask_list/', views.SubTaskList.as_view(), name='subtask-list'),
    path('subtask_list/add/', views.SubTaskCreateView.as_view(), name='subtask-add'),
    path('subtask_list/<int:pk>/', views.SubTaskUpdateView.as_view(), name='subtask-update'),
    path('subtask_list/<int:pk>/delete/', views.SubTaskDeleteView.as_view(), name='subtask-delete'),
]