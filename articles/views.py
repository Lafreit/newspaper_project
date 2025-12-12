# articles/views.py
from django.views.generic import ListView, DetailView # for list and detail views
from django.views.generic.edit import UpdateView, CreateView, DeleteView # for edit, create, and delete views
from django.urls import reverse_lazy # for redirecting after delete
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html' # specify your template name/location

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html' # specify your template name/location

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'body'] # fields to be edited
    template_name = 'article_edit.html' # specify your template name/location
    
    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.pk}) # redirect to article detail after edit

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html' # specify your template name/location
    success_url = reverse_lazy('article_list') # redirect to article list after deletion

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'body', 'author'] # fields to be created
    template_name = 'article_new.html' # specify your template name/location

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.pk}) # redirect to article detail after creation