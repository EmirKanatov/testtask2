from django.contrib import admin

from todoapp.models import TodoList, Todo, Comment

# Register your models here.


admin.site.register(TodoList)
admin.site.register(Todo)
admin.site.register(Comment)
