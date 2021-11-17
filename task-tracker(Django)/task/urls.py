from django.urls import path
from .  views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'), 
    path('logout/', LogoutView.as_view(next_page='task-list'), name='logout'), 
    path('', TaskList.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
]