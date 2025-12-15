# articles/urls.py
from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'), # URL pattern for article edit view
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'), # URL pattern for article detail view
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'), # URL pattern for article delete view
    path('new/', ArticleCreateView.as_view(), name='article_new'), # URL pattern for article create view
    path('', ArticleListView.as_view(), name='article_list'), # URL pattern for article list view
    # Comentários
    path("comment/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment_edit"), # URL pattern for comment edit view
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"), # URL pattern for comment delete view

]