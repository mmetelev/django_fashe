from django.urls import path
from . import views

urlpatterns = [

    path('<slug:slug>/<slug:product_slug>/', views.ProductDetailView.as_view(), name='products_detail'),
    path('<slug:slug>/', views.CategoryListView.as_view(), name='category_list'),
    path('', views.ProductListView.as_view(), name='products_list'),
]
