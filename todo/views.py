from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import ToDoModel

def home_view(request):
    todo_list = ToDoModel.objects.all()
    context = {'todo_list': todo_list}
    return render(request, 'todo/home.html', context)

def add_content_view(request):
    if request.method == 'POST':
        content = request.POST['content']
        if content:
            new_content = ToDoModel(content=content)
            new_content.save()
            return redirect('home_view')
    return redirect('home_view')

def delete_content_view(reqeust, id):
    content = ToDoModel.objects.get(id=id)
    content.delete()
    return redirect('home_view')
