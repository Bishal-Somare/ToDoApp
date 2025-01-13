from django.urls import path
from .views import TodoListCreateAPIView, TodoDetailView

urlpatterns = [
    path('todos/', TodoListCreateAPIView.as_view(), name='todo-list-create'),
    path('api/todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'), 

]
