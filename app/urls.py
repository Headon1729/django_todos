from django.contrib import admin
from django.urls import path
import app.views as views

urlpatterns = [
    path('hello/', views.hello),
    path('todos/', views.todos),
    path('todos/<str:id>', views.todo),
    path('todoss/', views.TodoListView.as_view()),
    path('todoss/<str:pk>', views.TodoDetailView.as_view()),
]
