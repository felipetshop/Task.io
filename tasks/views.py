from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tasks_list_view')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')
    

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks_list_view')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

@login_required
def tasks_list(request, status=None):
    tasks = Task.objects.filter(user=request.user)
    
    if status == 'pendente':
        tasks = tasks.filter(completed='pendente')
    elif status == 'concluído':
        tasks = tasks.filter(completed='concluído')
    tasks = tasks.order_by('-created_at')    
    return render(request, 'tasks/tasks_list.html', {
        'tasks': tasks,
        'show_filter_dropdown': True    
    })

@login_required
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'task/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)

    if request.method == 'POST':
        task.delete()
        return redirect('tasks_list_view')

    return render(request, 'tasks/delete_task.html', {'task': task})