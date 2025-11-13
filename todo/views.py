from django.shortcuts import redirect
from .models import Task

def addTask(request):
  task = request.POST['task']
  Task.objects.create(task=task) # Imposto il nome della task a quella passata nella POST (non inserisco anche is_completed perché è a False di default)
  return redirect('home')
