# articles/urls.py
from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article-edit'), # URL pattern for article edit view
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'), # URL pattern for article detail view
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'), # URL pattern for article delete view
    path('new/', ArticleCreateView.as_view(), name='article-create'), # URL pattern for article create view
    path('', ArticleListView.as_view(), name='article-list'), # URL pattern for article list view
]