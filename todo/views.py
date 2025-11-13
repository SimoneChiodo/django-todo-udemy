from django.shortcuts import get_object_or_404, redirect
from .models import Task

def addTask(request):
  task = request.POST['task']
  Task.objects.create(task=task) # Imposto il nome della task a quella passata nella POST (non inserisco anche is_completed perché è a False di default)
  return redirect('home')

def markAsDone(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.is_completed = True
  task.save()
  return redirect('home')

def markAsUndone(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.is_completed = False
  task.save()
  return redirect('home')