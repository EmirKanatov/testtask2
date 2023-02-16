from django.db import models
from django.utils import timezone

from todoapp.todo_model_settings import TodoStatuses, TodoImportance
from users.models import User


# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=128, default="untitled")
    created_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        User, null=True, related_name="todolists", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return self.title

    def count(self):
        return self.todos.count()

    def count_finished(self):
        return self.todos.filter(is_finished=True).count()

    def count_open(self):
        return self.todos.filter(is_finished=False).count()


class Todo(models.Model):
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    description = models.CharField('описание', max_length=128)
    is_finished = models.BooleanField('задача завершена?', default=False)
    importance = models.CharField(max_length=128, choices=TodoImportance.choices(), default=TodoImportance.FOURTH,
                                  verbose_name="важность")

    created_at = models.DateTimeField('создано', auto_now=True)
    plannedStartDate = models.DateTimeField('Запланировано начать')
    plannedEndDate = models.DateTimeField('Запланировано закончить')
    actualStartDate = models.DateTimeField('реально начато', null=True, blank=True)
    actualEndDate = models.DateTimeField('реально закончено', null=True, blank=True)

    status = models.CharField(max_length=250, choices=TodoStatuses.choices(), default=TodoStatuses.NOT_DONE,
                              verbose_name="Статус задачи")
    creator = models.ForeignKey(
        User, null=True, related_name="todo", on_delete=models.CASCADE, verbose_name='Пользователь'
    )
    todolist = models.ForeignKey(
        TodoList, related_name="todos", on_delete=models.CASCADE, verbose_name="список дел", null=True
    )
    #
    # class Meta:
    #     ordering = ["created_at", "importance"]

    def __str__(self):
        return self.description

    def get_status_display(self):
        for choice in TodoStatuses.choices():
            if choice[0] == self.status:
                return choice[1]

    def get_file(self):
        return self.files

    def close(self):
        self.status = True
        self.finished_at = timezone.now()
        self.save()

    def reopen(self):
        self.is_finished = False
        self.finished_at = None
        self.save()


class TodoFile(models.Model):

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

    todo = models.ForeignKey(Todo, related_name="files", blank=True, null=True, on_delete=models.CASCADE, verbose_name='задача')
    file = models.FileField(null=True, blank=True, verbose_name="файл")



class Comment(models.Model):
    text = models.TextField('текст', null=True, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='user_comment', verbose_name='автор')
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE,
                             related_name='comments', verbose_name='задача')

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.text