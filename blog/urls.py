from django.urls import path
# from .views import (
# article_detail_view, article_list_view, article_search_view,
# )
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, article_delete_view

app_name = 'blog'
urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name="article-create"),
    path('<int:id>/search/', ArticleDetailView.as_view(), name="article-detail"),
    path('<int:id>/update', ArticleUpdateView.as_view(), name="article-update"),
    path('<int:id>/delete', ArticleDeleteView.as_view(), name="article-delete"),
    path('', ArticleListView.as_view(), name="article-list"),
]