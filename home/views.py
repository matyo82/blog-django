from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages

# Create your views here.
def home(request):
    all = Todo.objects.all()
    return render(request, 'index.html', {'all':all})
def post(request, id_post):
    post = Todo.objects.get(id=id_post)
    return render(request, 'post.html', {'post':post})

def delete(request, Todo_id):
    Todo.objects.get(id=Todo_id).delete()
    messages.success(request, 'delete the post success!!', 'success')
    return redirect('home')