import django_filters
from . models import Student

class StudentFilter(django_filters.FilterSet):
    age_lt=django_filters.NumberFilter(field_name='age',lookup_expr='lt')
    age_gt=django_filters.NumberFilter(field_name='age',lookup_expr='gt')
    class Meta:
        model = Student
        fields = []  # Keep it empty if you're only using custom filters like above