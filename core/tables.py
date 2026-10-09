from crud_views.lib.table import Table

from .models import Employee, EmploymentType, ProductivityGoal


class EmployeeTable(Table):

    class Meta:
        model = Employee
        fields = ["last_name", "first_name", "email", "is_active"]
        template_name = "django_tables2/bootstrap5.html"
        attrs = {"class": "table table-vcenter card-table"}
        empty_text = "No employees found."


class EmploymentTypeTable(Table):

    class Meta:
        model = EmploymentType
        fields = ["code", "name", "default_minimum_hours", "is_active"]
        template_name = "django_tables2/bootstrap5.html"
        attrs = {"class": "table table-vcenter card-table"}
        empty_text = "No employment types found."


class ProductivityGoalTable(Table):

    class Meta:
        model = ProductivityGoal
        fields = [
            "employee",
            "employment_type",
            "minimum_hours",
            "effective_from",
            "effective_to",
        ]
        template_name = "django_tables2/bootstrap5.html"
        attrs = {"class": "table table-vcenter card-table"}
        empty_text = "No productivity goals found."
