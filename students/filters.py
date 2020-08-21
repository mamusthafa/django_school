import django_filters
from django_filters import DateFilter, CharFilter
from .models import Faculty

class OrderFilter(django_filters.FilterSet):
    startdate = DateFilter(field_name='date_posted', lookup_expr='gte')
    enddate = DateFilter(field_name='date_posted', lookup_expr='lte')
    fac_fname = CharFilter(field_name='fac_fname', lookup_expr='icontains')
    department = CharFilter(field_name='department', lookup_expr='icontains')
    class Meta:
        model = Faculty
        fields = ('fac_fname','department','faculty_id')
