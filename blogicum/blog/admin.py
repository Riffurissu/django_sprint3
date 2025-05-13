# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Location, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    list_filter = ('is_published',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'slug', 'is_published')
        }),
    )

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_published',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'is_published', 'category', 'location')
    search_fields = ('title', 'text')
    list_filter = ('is_published', 'category', 'location')
    raw_id_fields = ('author',)
    date_hierarchy = 'pub_date'
    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'pub_date', 'author', 'category', 'location', 'is_published')
        }),
    )

admin.site.site_header = 'Блог'
admin.site.index_title = 'Блог'
admin.site.site_title = 'Блог'