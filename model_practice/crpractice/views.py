from django.shortcuts import render, redirect, get_object_or_404
from .models import MyClass, Category, Article
from django.core.exceptions import ObjectDoesNotExist # get()요청의 예외처리 except: ObjectDoesNoteExist

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
    target_category = get_object_or_404(Category, pk=category_pk)
    titles = Article.objects.filter(category=target_category).exclude(is_deleted=True)
    # article_list = []
    # for title in titles:
    #     if title.is_deleted == False:
    #         article_list.append(title)
    context = {
        'target_category': target_category,
        'titles': titles
    }
    return render(request, 'categories.html', context)

def detail(request, title_pk):
    target_title = get_object_or_404(Article, pk=title_pk)
    target_category = get_object_or_404(Category, name=target_title.category)
    context = {
        'target_category_pk': target_category.pk,
        'target_title': target_title
    }
    return render(request, 'detail.html', context)

def add(request, category_pk):
    categories = Category.objects.all()
    error = {
        'error': False,
        'msg': ''
    }
    context = {
        'categories': categories,
        'category_pk': category_pk,
        'error': error
    }
    # print(type(Category.objects.all()))
    if request.method == 'POST':
        print(request.POST)
        # category = Category.objects.get(pk=category_pk)
        selected_category_name = request.POST['category']
        category = get_object_or_404(Category, name=selected_category_name)
        topic = request.POST['title']
        author = request.POST['author']
        content = request.POST['content']
        if (topic == '' or author == '' or content == '' or selected_category_name == 'null'):
            context['error']['error'] = True
            context['error']['msg'] = '모두 입력해주세요!'
        else:
            Article.objects.create(
                category = category,
                topic = topic,
                author = author,
                content = content
            )
        if category_pk == 0:
            return redirect('categories', category.pk)
        return redirect('categories', category.pk)
            
    return render(request, 'add.html', context)

def edit(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    error = {
        'error': False,
        'msg': ''
    }
    context = {
        'article_pk': article_pk,
        'article': article,
        'error': error
    }
    if request.method == 'POST':
        topic = request.POST['title']
        author = request.POST['author']
        content = request.POST['content']
        if (topic == '' or author == '' or content == ''):
            context['error']['error'] = True
            context['error']['msg'] = '모든 내용을 입력해주세요!!!'
        else:
            Article.objects.filter(pk=article_pk).update(
                topic = topic,
                author = author,
                content = content
            )
            return redirect('detail', article_pk)
    return render(request, 'edit.html', context)

def delete(request, article_pk):
    target_article = Article.objects.filter(pk=article_pk)
    category_pk = target_article.first().category.pk
    target_article.update(is_deleted=True)

    return redirect('categories', category_pk)