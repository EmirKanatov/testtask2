from rest_framework import serializers

from users.models import User
from .models import TodoList, Todo
from .todo_model_settings import TodoImportance


# class CreatorSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ('id', 'email', 'username', 'phone',)


class ToDoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = "__all__"


class ToDoSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    importance = serializers.SerializerMethodField()


    class Meta:
            model = Todo
            fields = "__all__"

    def get_status(self, obj):
        return obj.get_status_display()

    def get_importance(self, obj):
        return obj.get_importance_display()


class ToDoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
            model = Todo
            fields = "__all__"


class ToDoListDetailSerializer(serializers.ModelSerializer):
    todos = ToDoSerializer(many=True)


    class Meta:
        model = TodoList
        fields = "__all__"

    # def get_todos(self, instance):
    #     list_id = self.context.get('view').kwargs.get('pk')
    #   return 1