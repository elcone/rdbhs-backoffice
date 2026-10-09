import django_filters
from django import forms
from django.db.models import Q

from .models import Employee, EmploymentType, ProductivityGoal


class EmployeeFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method="filter_search",
        label="Search",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Name or email"}
        ),
    )
    is_active = django_filters.BooleanFilter(
        label="Active",
        widget=forms.NullBooleanSelect(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Employee
        fields = ["search", "is_active"]

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(first_name__icontains=value)
            | Q(last_name__icontains=value)
            | Q(email__icontains=value)
        )


class EmploymentTypeFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method="filter_search",
        label="Search",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Code or name"}
        ),
    )
    is_active = django_filters.BooleanFilter(
        label="Active",
        widget=forms.NullBooleanSelect(attrs={"class": "form-select"}),
    )

    class Meta:
        model = EmploymentType
        fields = ["search", "is_active"]

    def filter_search(self, queryset, name, value):
        return queryset.filter(Q(code__icontains=value) | Q(name__icontains=value))


class ProductivityGoalFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method="filter_search",
        label="Employee search",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Name or email"}
        ),
    )
    employment_type = django_filters.ModelChoiceFilter(
        queryset=EmploymentType.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    effective_from = django_filters.DateFilter(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )

    class Meta:
        model = ProductivityGoal
        fields = ["search", "employment_type", "effective_from"]

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(employee__first_name__icontains=value)
            | Q(employee__last_name__icontains=value)
            | Q(employee__email__icontains=value)
        )
