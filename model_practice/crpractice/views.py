from django.shortcuts import render
from .models import MyClass

# Create your views here.
def index(request):
    classes = MyClass.objects.all()
    context = {
        'classes': classes
    }
    return render(request, 'index.html', context)