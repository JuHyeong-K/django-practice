from django.db.models.query import NamedValuesListIterable
from django.urls import path
from .views import CategoryView, CategoryNameView , ArticleView, ArticleDetailView, ArticleEditView
app_name = 'blog'

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/<str:category_name>/', CategoryNameView.as_view(), name='categories_name'),
    path('categories/<str:category_name>/<int:detail_pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('categories/<str:category_name>/<int:detail_pk>/edit', ArticleEditView.as_view(), name='article_edit'),
    path('articles/',ArticleView.as_view(), name='articles'),
]