from django.contrib import admin
# Register your models here.
from django.utils.safestring import mark_safe

from .models import Product, ProductImage


class InLineProductImage(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', )


class ProductAdmin(admin.ModelAdmin):
    inlines = [InLineProductImage,]
    list_display = ('title', 'in_stock', 'price', 'image')
    list_filter = ('category',)
    search_fields = ['title']

    def image(self, obj):
        img = obj.images.first()
        if img:
            return mark_safe(f"<img src='{img.image.url}' width ='80', height='80', style='object-fit: contain' />")


admin.site.register(Product, ProductAdmin)
