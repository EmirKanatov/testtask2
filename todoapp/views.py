from django.shortcuts import render
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from filters.mixins import FiltersMixin
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
import django_filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.utils import timezone

from todoapp.filter import TodoListFilter, TodoFilter
from todoapp.models import TodoList, Todo
from todoapp.serializers import ToDoListSerializer, ToDoListDetailSerializer, ToDoSerializer, ToDoUpdateSerializer


class CharFilterInFilter(django_filters.BaseInFilter, django_filters.CharFilter):
    pass


# Create your views here.

class ToDoListViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = TodoListFilter


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
    fiter_backends = [DjangoFilterBackend]
    filterset_class = TodoFilter

    def perform_create(self, serializer):
        todolist = TodoList.objects.get(id=self.kwargs.get('list_pk'))
        serializer.save(todolist=todolist)

    def get_queryset(self):
        return Todo.objects.filter(todolist=self.kwargs.get('list_pk'))

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = ToDoUpdateSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)