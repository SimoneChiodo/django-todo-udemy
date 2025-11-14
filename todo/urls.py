from django.urls import path
from . import views

urlpatterns = [
  path('addTask/', views.addTask, name='addTask'),
  
  # Mark as Done
  path('markAsDone/<int:pk>/', views.markAsDone, name='markAsDone'),
  
  # Mark as Undone
  path('markAsUndone/<int:pk>/', views.markAsUndone, name='markAsUndone'),

  # Edit Feature
  path('edit_task/<int:pk>/', views.editTask, name='editTask'),
]
