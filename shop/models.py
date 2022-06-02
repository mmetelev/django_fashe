from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Category"""
    name = models.CharField('category', max_length=100)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    slug = models.SlugField('category url', max_length=100, unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product"""
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    main_image = models.ImageField('product image', upload_to='products/%Y/%m/%d')
    name = models.CharField('product name', max_length=50)
    after_price_text = models.TextField('product text ', max_length=200)
    description_text = models.TextField('product description', max_length=500)
    additional_text = models.TextField('product additional info', max_length=1000)
    price = models.DecimalField('product price', max_digits=10, decimal_places=2)
    sale_price = models.DecimalField('sale product price', max_digits=10, decimal_places=2)
    tags = TaggableManager()
    is_active = models.CharField('product visibility', max_length=15, choices=STATUS_CHOICES, default='published')
    is_featured = models.BooleanField('featured Product', default=False)
    is_sale = models.BooleanField('sale product', default=False)
    is_new = models.BooleanField('product is new', default=True)
    slug = models.SlugField('product url', max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products_detail',
                       kwargs={'slug': self.category.name, 'product_slug': self.slug})


class ColorSize(models.Model):
    """Color size and product quantity"""
    size = models.CharField('product size', max_length=10)
    color = models.CharField('product color', max_length=15)
    stock = models.PositiveIntegerField('product quantity')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='product'
    )


class SlickImage(models.Model):
    """For additional product image in detail section"""
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='additional product image'
    )

    def __str__(self):
        return self.product


class Review(models.Model):
    """Product reviews"""
    name = models.CharField('review author name', max_length=50)
    message = models.TextField('review message', max_length=500)
    email = models.EmailField('author Email', max_length=100)
    product = models.ForeignKey(
        Product,
        related_name='review',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField('created at', auto_now_add=True)
    is_active = models.BooleanField('reviews visibility', default=True)

    def __str__(self):
        return self.name


class Arrival(models.Model):
    """New arrivals product"""
    image = models.ImageField('new arrival product image', upload_to='arrival/%Y/%m/%d')
    name = models.TextField('new arrival', max_length=200)

    def __str__(self):
        return self.name
