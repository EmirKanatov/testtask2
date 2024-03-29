# Generated by Django 4.1.6 on 2023-02-08 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='untitled', max_length=128)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todolists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=128, verbose_name='описание')),
                ('is_finished', models.BooleanField(default=False, verbose_name='задача завершена?')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='создано')),
                ('plannedStartDate', models.DateTimeField(null=True, verbose_name='Запланировано начать')),
                ('plannedEndDate', models.DateTimeField(null=True, verbose_name='Запланировано закончить')),
                ('actualStartDate', models.DateTimeField(null=True, verbose_name='реально начато')),
                ('actualEndDate', models.DateTimeField(null=True, verbose_name='реально закончено')),
                ('status', models.CharField(choices=[('Не выполнено', 'Не выполнено'), ('В процессе', 'В процессе'), ('Выполнено', 'Выполнено')], default='Не выполнено', max_length=250, verbose_name='Статус задачи')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todo', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('todolist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='todoapp.todolist', verbose_name='список дел')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='todoapp.todo', verbose_name='коментарии')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
