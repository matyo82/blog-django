from django.shortcuts import render
from .models import Todo
# Create your views here.
def home(request):
    person = {'name':'matin'}
    all = Todo.objects.all()
    return render(request, 'index.html', {'all':all})
def post(request, id_post):
    post = Todo.objects.get(id=id_post)
    return render(request, 'post.html', {'post':post})
