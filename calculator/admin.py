from django.contrib import admin  # type: ignore[reportMissingModuleSource]
from .models import ToyProduct, BlogPost

@admin.register(ToyProduct)
class ToyProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'original_price', 'original_price_year', 'popular']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['category', 'popular']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'published']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['published']