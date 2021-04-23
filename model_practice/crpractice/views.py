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

def categories(request, category_pk):
    target_category = Category.objects.get(pk=category_pk)
    titles = Article.objects.filter(category=target_category)
    context = {
        'target_category': target_category,
        'titles': titles
    }
    return render(request, 'categories.html', context)

def detail(request, title_pk):
    target_title = Article.objects.get(pk=title_pk)
    context = {
        'target_title': target_title
    }
    return render(request, 'detail.html', context)