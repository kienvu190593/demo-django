import django_filters
from categories.models import *

class GroupProductFilter(django_filters.FilterSet):
    code = django_filters.CharFilter(field_name='code', lookup_expr='contains')
    name = django_filters.CharFilter(field_name='name', lookup_expr='contains')
    create_date_from = django_filters.DateTimeFilter(field_name='dateCreate', lookup_expr='gte')
    create_date_to = django_filters.DateTimeFilter(field_name='dateCreate', lookup_expr='lte')

    class Meta:
        models = GroupProductTbl
        fields = ['code', 'name', 'create_date_from', 'create_date_to']