from django.contrib import admin

from eshop.product.models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_editable = ('name', 'category')


admin.site.register(Category)
