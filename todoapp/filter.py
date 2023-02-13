import django_filters

from todoapp.models import TodoList, Todo
from todoapp.todo_model_settings import TodoStatuses

TODOFILTERSTATUSES = (
    ('not_done', 'Не выполнено'),
    ('in_progress', 'В процессе'),
    ('done', 'Выполнено'),
)



class TodoListFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr="icontains")
    created_at = django_filters.DateFilter(field_name='created_at', lookup_expr='date')
    created_at__gte = django_filters.DateFilter(field_name='created_at', lookup_expr='date__gte')
    created_at__lte = django_filters.DateFilter(field_name='created_at', lookup_expr='date__lte')

    class Meta:
        model = TodoList
        fields = ['title', 'created_at', ]


class TodoFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(field_name='description', lookup_expr="icontains", )
    created_at = django_filters.DateFilter(field_name='created_at', lookup_expr='date')
    created_at__gte = django_filters.DateFilter(field_name='created_at', lookup_expr='date__gte')
    created_at__lte = django_filters.DateFilter(field_name='created_at', lookup_expr='date__lte')
    plannedStartDate = django_filters.DateFilter(field_name='plannedStartDate', lookup_expr='date')
    plannedEndDate = django_filters.DateFilter(field_name='plannedEndDate', lookup_expr='date')
    actualStartDate = django_filters.DateFilter(field_name='actualStartDate', lookup_expr='date')
    actualEndDate = django_filters.DateFilter(field_name='actualEndDate', lookup_expr='date')
    status = django_filters.ChoiceFilter(choices=TodoStatuses.choices())
    o = django_filters.OrderingFilter(
        fields=(
            ('importance', 'importance'),
        ),
    )



class Meta:
        model = Todo
        fields = ['description', 'created_at', 'plannedStartDate', 'plannedEndDate',
                  'actualStartDate', 'actualEndDate', 'status', 'o']
