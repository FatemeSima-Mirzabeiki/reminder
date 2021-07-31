from django.contrib import admin
from .models import Category, Task

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'due_date']
    list_display_links = ['title']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'priority', 'category', 'due_date', 'done', 'slug')
        }),

    )


