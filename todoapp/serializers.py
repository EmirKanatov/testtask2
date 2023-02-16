from rest_framework import serializers

from users.models import User
from .models import TodoList, Todo, Comment, TodoFile
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


class ToDoListDetailCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoFile
        fields = ("file",)


class ToDoSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    importance = serializers.SerializerMethodField()
    files = FileSerializer(many=True, required=False)

    class Meta:
        model = Todo
        fields = "__all__"

    def get_file(self, obj):
        return obj.get_file()

    def get_status(self, obj):
        return obj.get_status_display()

    def get_importance(self, obj):
        return obj.get_importance_display()


class ToDoDetailSerializer(ToDoSerializer):
    comments = ToDoListDetailCommentSerializer(many=True)


class ToDoUpdateSerializer(serializers.ModelSerializer):
    files = FileSerializer()

    class Meta:
            model = Todo
            fields = "__all__"


class ToDoListDetailSerializer(serializers.ModelSerializer):
    todos = ToDoSerializer(many=True)

    class Meta:
        model = TodoList
        fields = "__all__"
