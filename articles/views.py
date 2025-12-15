# articles/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # for login and permission handling
from django.core.exceptions import PermissionDenied # for permission handling
from django.shortcuts import redirect # for redirecting
from django.views.generic import ListView, DetailView # for list and detail views
from django.views.generic.edit import UpdateView, CreateView, DeleteView # for edit, create, and delete views
from django.urls import reverse_lazy # for redirecting after delete
from .models import Article, Comment
from.forms import CommentForm

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html' # specify your template name/location
    login_url = '/accounts/login/'  # redirect to login if not authenticated

#----------------------------------
# Detalhe do artigo + comentários
#----------------------------------
class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html' # specify your template name/location
    login_url = '/accounts/login/'  # redirect to login if not authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
            return redirect("login")

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.article = self.object
            comment.save()
            return redirect("article_detail", pk=self.object.pk)

        context = self.get_context_data(form=form)
        return self.render_to_response(context)
# ---------------------------
# EDITAR COMENTÁRIO
# ---------------------------
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ("comment",)
    template_name = "comment_edit.html"

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user or self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy("article_detail", kwargs={"pk": self.object.article.pk})

# ---------------------------
# EXCLUIR COMENTÁRIO
# ---------------------------
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "comment_delete.html"

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user or self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy("article_detail", kwargs={"pk": self.object.article.pk})
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