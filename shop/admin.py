from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin

from .models import Category, Product, Review, Arrival, ColorSize, SlickImage


@admin.register(ColorSize)
class ColorSizeAdmin(admin.ModelAdmin):
    """Color and size admin"""
    list_display = ('size', 'color', 'stock', 'product')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Products admin"""
    list_display = ('name', 'category', 'get_image')
    readonly_fields = ('get_image',)
    prepopulated_fields = {'slug': ('name',)}

    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.main_image.url} width="100" height="120"')

    get_image.short_description = 'Product image'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Reviews admin"""
    pass


@admin.register(Arrival)
class ArrivalAdmin(admin.ModelAdmin):
    """New arrival admin"""
    pass


@admin.register(SlickImage)
class SlickImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="120"')

    get_image.short_description = 'Product image'


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


