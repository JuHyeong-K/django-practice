from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Article, Like, Member, Comment, RelationShip
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

def detail(request, article_pk, error_status):
    target_article = get_object_or_404(Article, pk=article_pk)
    target_category = get_object_or_404(Category, name=target_article.category.name)
    comments = Comment.objects.filter(article=target_article).exclude(is_deleted=True)
    context = {
        'target_category_pk': target_category.pk,
        'target_article': target_article,
        'comments': comments,
        'error': {
            'status': error_status,
            'msg': ''
        }
    }
    if request.method == 'GET' and context['error']['status'] == 'True':
        context['error']['msg'] = 'MISSING_CONTEXT'
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
    context = {
        'error': {
            'state': False,
            'msg': ''
        }
    }
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_pw_check = request.POST['user_pw_check']

        member_name = request.POST['member_name']
        member_intro = request.POST['member_intro']

        user_id_check = User.objects.filter(username=user_id)
        print(user_id_check, len(user_id_check))


        if (not user_id or not user_pw or not user_pw_check):
            context['error']['state'] = True
            context['error']['msg'] = 'ID_PW_MISSING'
            return render(request, 'signup.html', context)


        if len(user_id_check) != 0:
            context['error']['state'] = True
            context['error']['msg'] = 'ID_EXIST'
            return render(request, 'signup.html', context)


        if user_pw != user_pw_check:
            context['error']['state'] = True
            context['error']['msg'] = 'PW_CHECK'
            return render(request, 'signup.html', context)

        user = User.objects.create_user(username=user_id, password=user_pw)
        Member.objects.create(
            user_id=user,
            name=member_name,
            content=member_intro
        )
        RelationShip.objects.create(
            member=user
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
                if user != None:
                    login(request, user)
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
    return redirect('index')

def comment_add(request, article_pk):
    error_status = False
    target_article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        content = request.POST['comment_content']
        if content == '':
            error_status = True
            return redirect('detail', article_pk, error_status)            
    Comment.objects.create(
        article=target_article,
        writer=request.user,
        content=content
    )
    return redirect('detail', article_pk, error_status)

def comment_delete(request, comment_pk):
    error_status = False
    # target_comment = get_object_or_404(Comment, pk=comment_pk) 
    target_comment = Comment.objects.filter(pk=comment_pk) # update는 querySet 함수다.
    article_pk = target_comment.first().article.pk
    target_comment.update(is_deleted=True)
    return redirect('detail', article_pk, error_status)

def mypage(request):
    categories = Category.objects.all()
    articles = Article.objects.filter(author=request.user).exclude(is_deleted=True)
    comments = Comment.objects.filter(writer=request.user).exclude(is_deleted=True)
    context = {
        'categories': categories,
        'articles': articles,
        'comments': comments
    }
    return render(request, 'mypage.html', context)

def mypage_article_delete(request, article_pk):
    target_article = Article.objects.filter(pk=article_pk)
    comments_of_article = Comment.objects.filter(article=target_article.first())
    target_article.update(is_deleted=True)
    comments_of_article.update(is_deleted=True)

    return redirect('mypage')

def mypage_comment_delete(request, comment_pk):
    target_comment = Comment.objects.filter(pk=comment_pk)
    target_comment.update(is_deleted=True)
    return redirect('mypage')

def following(request, article_pk):
    error_status = False
    target_article = Article.objects.filter(pk=article_pk).first()
    follow = RelationShip.objects.filter(member=target_article.author).first()
    if request.user in follow.follower.all():
        follow.follower.remove(request.user)
        return redirect('detail', article_pk, error_status)
    follow.follower.add(request.user)
    return redirect('detail', article_pk, error_status)
    
def like(request, comment_pk):
    error_status = False
    target_comment = Comment.objects.filter(pk=comment_pk).first()
    like = Like.objects.filter(comment=target_comment).first()
    if request.user in like.member.all():
        like.member.remove(request.user)
        return redirect('detail', target_comment.article.pk, error_status)

    like.member.add(request.user)
    return redirect('detail', target_comment.article.pk, error_status)
    