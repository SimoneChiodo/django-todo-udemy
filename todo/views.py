from django.shortcuts import get_object_or_404, redirect, render
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

def editTask(request, pk):
  get_task = get_object_or_404(Task, pk=pk)
  if request.method == 'POST':
    get_task.task = request.POST['task']
    get_task.save()
    return redirect('home')
  else:
    context = {
      'get_task': get_task
    }
  return render(request, 'editTask.html', context)


def deleteTask(request, pk):
  get_task = get_object_or_404(Task, pk=pk)
  get_task.delete()
  return redirect('home')
