from django.urls import path
from . import views

urlpatterns = [
  path('addTask/', views.addTask, name='addTask'),
  path('markAsDone/<int:pk>/', views.markAsDone, name='markAsDone'),
]
