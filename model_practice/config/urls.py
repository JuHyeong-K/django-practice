"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crpractice import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('categories/<int:category_pk>/', views.categories, name='categories'),
    path('detail/<int:article_pk>/<str:error_status>/', views.detail, name='detail'),
    path('add/<int:category_pk>/', views.add, name='add'),
    path('edit/<int:article_pk>/', views.edit, name='edit'),
    path('delete/<int:article_pk>/', views.delete, name='delete'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_views, name='login'),
    path('logout/', views.logout_views, name='logout'),
    path('comment_add/<int:article_pk>/', views.comment_add, name='comment_add'),
    path('comment_delete/<int:comment_pk>/', views.comment_delete, name='comment_delete'),
    path('mypage/', views.mypage, name='mypage'),
    path('mypage_article_delete/<int:article_pk>', views.mypage_article_delete, name='mypage_article_delete'),
    path('mypage_comment_delete/<int:comment_pk>', views.mypage_comment_delete, name='mypage_comment_delete'),
    path('following/<int:article_pk>', views.following, name='following'),
    path('like/<int:comment_pk>', views.like, name='like'),
]
