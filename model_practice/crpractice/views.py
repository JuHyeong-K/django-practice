from django.shortcuts import render
from .models import MyClass, Category, Article

# Create your views here.
def index(request):
    classes = MyClass.objects.all()
    categories = Category.objects.all()
    context = {
        'classes': classes,
        'categories': categories
    }
    return render(request, 'index.html', context)

def categories(request):
    print(request)
    return render(request, 'categories.html')

def detail(request):
    return render(request, 'detail.html')