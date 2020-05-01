import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr="gte")
    note = CharFilter(field_name="note", lookup_expr="icontains")

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['address', 'date_created', 'customer']


class ProductFilter(django_filters.FilterSet):
    description = CharFilter(field_name='description', lookup_expr='')

    class Meta:
        model = Products
        fields = '__all__'
        exclude = ['date_created','tags']
