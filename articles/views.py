# articles/views.py
from django.contrib.auth.mixins import LoginRequiredMixin # for requiring login
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView # for list and detail views
from django.views.generic.edit import UpdateView, CreateView, DeleteView # for edit, create, and delete views
from django.urls import reverse_lazy # for redirecting after delete
from .models import Article

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html' # specify your template name/location
    login_url = '/accounts/login/'  # redirect to login if not authenticated

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html' # specify your template name/location
    login_url = '/accounts/login/'  # redirect to login if not authenticated

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'body'] # fields to be edited
    template_name = 'article_edit.html' # specify your template name/location
    login_url = '/accounts/login/'  # redirect to login if not authenticated

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.pk}) # redirect to article detail after edit
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html' # specify your template name/location
    success_url = reverse_lazy('article_list') # redirect to article list after deletion
    login_url = '/accounts/login/'  # redirect to login if not authenticated

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'body', 'author'] # fields to be filled in the form
    template_name = 'article_new.html'
    login_url = '/accounts/login/'  # redirect to login if not authenticated

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)