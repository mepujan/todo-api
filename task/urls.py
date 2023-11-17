from django.urls import path, include
from .views import TaskCreateAPIView, TaskRetriveUpdateDeleteAPIView


urlpatterns = [
    path('tasks/', TaskCreateAPIView.as_view(), name='tasks'),
    path('task/<int:pk>', TaskRetriveUpdateDeleteAPIView.as_view(), name='task')
]
