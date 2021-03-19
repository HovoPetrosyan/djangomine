from django.contrib import admin

from store.models import Banner, Brand, Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'category', 'brand', 'in_stock', 'is_active', 'created']
    list_display_links = ['title', ]
    search_fields = ['title', 'category', 'brand', 'author']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['alt_text', ]
