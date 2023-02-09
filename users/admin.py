from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from users.models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'username', 'first_name', 'phone', 'is_verified', 'date_joined', 'is_active',)
    list_filter = ( 'is_verified',)
    list_editable = ('is_verified',)
    readonly_fields = ('date_joined', 'last_login',)
    fieldsets = (
        ('Основное', {'fields': (
            'email', 'username', 'first_name', 'last_name', 'phone', 'password',)}),
        ('Даты', {'fields': ('date_joined', 'last_login', 'birth_date')}),
        ('Разрешения', {'fields': ('is_superuser', 'is_verified', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active',)}
         ),
    )
    search_fields = ('email','username', 'phone', 'first_name', 'last_name')
    ordering = ('email',)
    list_display_links = ('email',)
    list_per_page = 10

    def get_ordering(self, request):
        return ['-date_joined']


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)

admin.site.site_header = ("ToDo App Admin")

