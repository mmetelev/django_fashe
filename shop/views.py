from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from cart.forms import CartAddProductForm
from .models import Product, Category


class ProductListView(ListView):
    """Product list"""
    paginate_by = 12
    model = Product

    def get_queryset(self):
        return Product.objects.filter(is_active='published')


class CategoryListView(ListView):
    """List of categories"""
    paginate_by = 12
    model = Product

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')


class ProductDetailView(DetailView):
    """Product detail"""
    model = Product
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'
    cart_product_form = CartAddProductForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = self.object.tags.similar_objects()
        context['cart_product_form '] = CartAddProductForm()
        return context

# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(is_active='published')
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request, 'shop/product_list.html',
#                   {'category': category, 'categories': categories, 'products': products})
#
#
# def product_detail(request, id, slug):
#     product = get_object_or_404(Product,
#                                 id=id,
#                                 slug=slug,
#                                 available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request, 'shop/product_detail.html', {'product': product,
#                                                         'cart_product_form': cart_product_form})
