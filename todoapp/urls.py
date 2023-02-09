from django.urls import path, include
from rest_framework_nested.routers import NestedSimpleRouter, SimpleRouter

from .views import ToDoListViewSet, TodoViewSet

router = SimpleRouter()
router.register(r'todolists', ToDoListViewSet, basename='todolists')

domains_router = NestedSimpleRouter(router, r'todolists', lookup='list')
domains_router.register(r'todo', TodoViewSet, basename='todos')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(domains_router.urls)),

]