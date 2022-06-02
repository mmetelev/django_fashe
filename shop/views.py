from django.views.generic import ListView, DetailView

from .models import Product


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = self.object.tags.similar_objects()
        return context
