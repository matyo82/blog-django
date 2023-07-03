from django.shortcuts import render
from .models import Todo
# Create your views here.
def home(request):
    person = {'name':'matin'}
    all = Todo.objects.all()
    return render(request, 'index.html', {'all':all})