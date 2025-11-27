from django.contrib import admin
from .models import Category, Post, Photo, Event, Member

# Register your models here.

class PhotoInLine(admin.TabularInline):
    model = Photo
    extra = 1

#Admin para Posts
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'is_published')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PhotoInLine]
    date_hierarchy = 'published_at'
    ordering = ('-published_at',)

#Admin para Categorias
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

#Admin para Eventos
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start', 'end', 'location')
    list_filter = ('start',)
    search_fields = ('title', 'description', 'location')

#Admin para Miembros
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'joined')
    search_fields = ('first_name', 'last_name', 'role')

