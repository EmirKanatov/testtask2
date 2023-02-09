from rest_framework import serializers

from users.models import User
from .models import TodoList, Todo


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