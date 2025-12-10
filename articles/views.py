# articles/views.py
from django.views.generic import ListView, DetailView # for list and detail views
from django.views.generic.edit import UpdateView, CreateView, DeleteView # for edit, create, and delete views
from django.urls import reverse_lazy # for redirecting after delete
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html' # specify your template name/location

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html' # specify your template name/location

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'body'] # fields to be edited
    template_name = 'articles/article_form.html' # specify your template name/location

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/article_confirm_delete.html' # specify your template name/location
    success_url = reverse_lazy('article-list') # redirect to article list after deletion

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'body'] # fields to be created
    template_name = 'articles/article_form.html' # specify your template name/location