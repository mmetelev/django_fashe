from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Category"""
    name = models.CharField(max_length=100, verbose_name='Category')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=100, verbose_name='Category Url', unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product"""
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, blank=True, null=True)
    main_image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Product image')
    name = models.CharField(max_length=50, verbose_name='Product name')
    after_price_text = models.TextField(max_length=200, verbose_name='Product text ')
    description_text = models.TextField(max_length=500, verbose_name='Product description')
    additional_text = models.TextField(max_length=1000, verbose_name='Product additional info')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Product price')
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Sale product price')
    tags = TaggableManager()
    is_active = models.CharField(max_length=15, verbose_name='Product visibility',
                                 choices=(('draft', 'Draft'), ('published', 'Published')), default='published')
    is_featured = models.BooleanField(verbose_name='Featured Product', default=False)
    is_sale = models.BooleanField(verbose_name='Sale product', default=False)
    is_new = models.BooleanField(verbose_name='Product is new', default=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Product url')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products_detail',
                       kwargs={'slug': self.category.name, 'product_slug': self.slug})


class ColorSize(models.Model):
    """Color size and product quantity"""
    size = models.CharField(max_length=10, verbose_name='Product size')
    color = models.CharField(max_length=15, verbose_name='Product color')
    stock = models.PositiveIntegerField(verbose_name='Product quantity')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')


class SlickImage(models.Model):
    """For additional product image in detail section"""
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Additional product image')

    def __str__(self):
        return self.product


class Review(models.Model):
    """Product reviews"""
    name = models.CharField(max_length=50, verbose_name='Review author name')
    message = models.TextField(max_length=500, verbose_name='Review message')
    email = models.EmailField(max_length=100, verbose_name='Author Email')
    product = models.ForeignKey(Product, related_name='review', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    is_active = models.BooleanField(verbose_name='Reviews visibility', default=True)

    def __str__(self):
        return self.name


class Arrival(models.Model):
    """New arrivals product"""
    image = models.ImageField(upload_to='arrival/%Y/%m/%d', verbose_name='New arrival product image')
    name = models.TextField(max_length=200, verbose_name='New arrival')

    def __str__(self):
        return self.name
