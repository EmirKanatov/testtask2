from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from todoapp.models import TodoList, Todo
from todoapp.serializers import ToDoListSerializer, ToDoListDetailSerializer, ToDoSerializer


# Create your views here.

class ToDoListViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TodoList.objects.filter(creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


    def get_serializer_class(self):
        if self.action == 'list':
            return ToDoListSerializer
        if self.action == 'retrieve':
            return ToDoListDetailSerializer
        return ToDoListSerializer # I dont' know what you want for create/destroy/update.


class TodoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ToDoSerializer

    def perform_create(self, serializer):
        todolist = TodoList.objects.get(id=self.kwargs.get('list_pk'))
        serializer.save(todolist=todolist)

    def get_queryset(self):

        return Todo.objects.filter(todolist=self.kwargs.get('list_pk'))