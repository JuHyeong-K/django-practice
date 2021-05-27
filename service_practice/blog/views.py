from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic, View
from django.contrib.auth.mixins import  LoginRequiredMixin

from .models import Category, Article
from .services import EditDto, BlogService

# Create your views here.
class CategoryView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = Category
    context_object_name = 'categories'
    template_name = 'categories.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoryNameView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = Article
    context_object_name = 'article'
    template_name = 'articles.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = self.kwargs['category_name']
        context['target_articles'] = Article.objects.filter(category__name=self.kwargs['category_name'])
        return context

class ArticleView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = Article
    context_object_name = 'articles'
    template_name = 'articles.html'
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class ArticleDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
    model = Article
    context_object_name = 'article'
    template_name = 'detail.html'
    # def get_context_data(self, **kwargs):
    #     print(self.kwargs)
    #     context = super().get_context_data(**kwargs)
    #     return context
    def get_object(self):
        return get_object_or_404(Article, pk=self.kwargs['detail_pk'])

class ArticleEditView(LoginRequiredMixin, View):
    login_url = '/accounts/login'
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=self.kwargs['detail_pk'])
        return render(request, 'edit.html', {'article': article})
    
    def post(self, request, *args, **kwargs):
        edit_dto = self._build_edit_dto(request.POST)
        result = BlogService.edit(edit_dto)
        if result['error']['state']:
            return render(request, 'edit.html', result)
        return redirect(f"/blog/categories/{self.kwargs['category_name']}/{self.kwargs['detail_pk']}")

    def _build_edit_dto(self, post_data):
        return EditDto(article_pk=self.kwargs['detail_pk'], title=post_data['title'], content=post_data['content'])

# class EditView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'edit.html')
    
#     def post(self, request, *args, **kwargs):
#         @staticmethod
#         def _build_edit_dto(post_data):
#             return EditDto(
                
#             )
