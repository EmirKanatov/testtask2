from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from todoapp.models import TodoList, Todo, Comment, TodoFile


# Register your models here.


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title", "creator", "created_at",)
    search_fields = ("title__startswith", )
    list_filter = ("created_at", )
    readonly_fields = ("created_at",)
    fieldsets = (
        ('Основное', {'fields': (
            'title', 'created_at', 'creator',)}),
    )

admin.site.register(Todo)
admin.site.register(Comment)
admin.site.register(TodoFile)
