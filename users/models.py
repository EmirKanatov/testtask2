from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.core.validators import validate_email
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken

from .manager import UserManager


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        db_table = 'user'
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    USERNAME_FIELD = 'email'

    objects = UserManager()

    email = models.EmailField('Почта(email)', unique=True, null=True, blank=True, validators=(validate_email,))
    username = models.CharField('username', max_length=50, unique=True,
                                help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                null=True, blank=True)
    password = models.CharField('Пароль', max_length=128, null=True, blank=True)
    phone = PhoneNumberField('Номер телефона', unique=True, null=True, blank=True)
    first_name = models.CharField('Имя', max_length=250, null=True, blank=True)
    last_name = models.CharField('Фамилия', max_length=250, null=True, blank=True)
    description = models.TextField('О себе', max_length=1024, null=True, blank=True)
    date_joined = models.DateTimeField('Дата регистрации', auto_now_add=True)
    birth_date = models.DateField('Дата рождения', null=True, blank=True)

    is_verified = models.BooleanField("Польверждение пользователя", default=False)
    is_active = models.BooleanField('Активный', default=True)
    is_superuser = models.BooleanField('Суперпользователь', default=False)
    is_staff = models.BooleanField("Статус работника", default=False,
        help_text="Designates whether the user can log into this admin site.",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'{self.username}'

    def has_module_perms(self, module, *args, **kwargs):
        if not self.is_active:
            return False
        if self.is_superuser:
            return True
        return False

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

