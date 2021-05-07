from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Article, Member, Comment
from django.core.exceptions import ObjectDoesNotExist # get()요청의 예외처리 except: ObjectDoesNoteExist
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import re


# Create your views here.
def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
        }
    return render(request, 'index.html', context)

def categories(request, category_pk):
    target_category = get_object_or_404(Category, pk=category_pk)
    titles = Article.objects.filter(category=target_category).exclude(is_deleted=True)

    context = {
        'target_category': target_category,
        'titles': titles
    }
    return render(request, 'categories.html', context)

def detail(request, title_pk):
    target_article = get_object_or_404(Article, pk=title_pk)
    target_category = get_object_or_404(Category, name=target_article.category.name)
    context = {
        'target_category_pk': target_category.pk,
        'target_article': target_article
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
        author = request.user
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
        author = request.user
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

def signup(request):
    error_state = False
    error_msg = ''
    context = {
        'error': {
            'state': error_state,
            'msg': error_msg
        }
    }
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_pw_check = request.POST['user_pw_check']

        member_name = request.POST['member_name']
        member_intro = request.POST['member_intro']

        user_id_check = User.objects.filter(username=user_id)


        if (not user_id or not user_pw or not user_pw_check):
            error_state = True
            error_msg = 'ID_PW_MISSING'
            return render(request, 'signup.html', context)


        if len(user_id_check) != 0:
            error_state = True
            error_msg = 'ID_EXIST'
            return render(request, 'signup.html', context)


        if user_pw != user_pw_check:
            error_state = True
            error_msg = 'PW_CHECK'
            return render(request, 'signup.html', context)

        user = User.objects.create_user(username=user_id, password=user_pw)
        Member.objects.create(
            user_id=user,
            name=member_name,
            content=member_intro
        )
        return redirect('index')
        # if re.fullmatch(r'[A-Za-z0-9@#$%^&+~!]{8,}', user_pw):
        #     User.objects.create(username=user_id, password=user_pw)
        #     return redirect('index')
        # else:
        #     error_state = True
        #     error_msg = 'PW_CHECK_REQUIRED'

    return render(request, 'signup.html', context)

def login_views(request):
    context = {
        'error': {
            'state': False,
            'msg': ''
        },
    }
    if request.method == 'POST':
        login_id = request.POST['login_id']
        login_pw = request.POST['login_pw']
        print(login_id, login_pw)
        login_user = User.objects.filter(username=login_id)

        if (login_id and login_pw):
            if len(login_user) != 0:
                user = authenticate(
                    username=login_id,
                    password=login_pw
                )
                print(user)
                if user != None:
                    login(request, user)
                    print(request.user)
                    return redirect('index')
                else:
                    context['error']['state'] = True
                    context['error']['msg'] = 'PW_CHECK'
            else:
                context['error']['state'] = True
                context['error']['msg'] = 'ID_NOT_EXIST'
        else:
            context['error']['state'] = True
            context['error']['msg'] = 'ID_PW_MISSING'

    return render(request, 'login.html', context)

def logout_views(request):
    logout(request)
    print(request.user)
    return redirect('index')