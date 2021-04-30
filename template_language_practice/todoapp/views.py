from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)

def add(request):
    if request.method == 'POST':
        content = request.POST['content']
        Todo.objects.create(content=content)
        return redirect('index')
    return render(request, 'add.html')

def edit(request, todo_pk):
    # todo = get_object_or_404(Todo, pk=todo_pk)
    todo = Todo.objects.filter(pk=todo_pk)
    context = {
        'todos': Todo.objects.all(),
        'target_todo': todo.first()
    }
    if request.method == 'POST':
        edited_content = request.POST['edited_content']
        todo.update(content=edited_content)
        return redirect('index')
    return render(request, 'edit.html', context)

def completed(request, todo_pk):
    target_todo = Todo.objects.filter(pk=todo_pk)
    if target_todo.first().is_completed:
        target_todo.update(is_completed=False)
    else:
        target_todo.update(is_completed=True)
    print(target_todo.first().is_completed)
    return redirect('index')