from django.urls import path

from .views import (
product_search_view,
product_list_view,
ProductCreateView,
ProductUpdateView,
ProductDeleteView
)
app_name = "products"
urlpatterns = [
    path('create/', ProductCreateView.as_view(), name="product_create"),
    path('<int:id>/search/', product_search_view, name="product_detail"),
    path('<int:id>/update/', ProductUpdateView.as_view(), name="product_update"),
    path('<int:id>/delete/', ProductDeleteView.as_view(), name="product_delete"),
    path('', product_list_view, name="product_list"),
]