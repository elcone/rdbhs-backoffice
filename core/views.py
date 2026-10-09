from crud_views.lib.viewset import ViewSet

from .crud import (
    CrudCreateView,
    CrudDeleteView,
    CrudDetailView,
    CrudListView,
    CrudUpdateView,
)
from .filters import EmployeeFilter, EmploymentTypeFilter, ProductivityGoalFilter
from .forms import EmployeeForm, EmploymentTypeForm, ProductivityGoalForm
from .models import Employee, EmploymentType, ProductivityGoal
from .tables import EmployeeTable, EmploymentTypeTable, ProductivityGoalTable

employee_viewset = ViewSet(
    model=Employee,
    name="employee",
    prefix="employees",
)


class EmployeeListView(CrudListView):
    cv_viewset = employee_viewset
    table_class = EmployeeTable
    filterset_class = EmployeeFilter


class EmployeeDetailView(CrudDetailView):
    cv_viewset = employee_viewset
    template_name = "core/employee/detail.html"


class EmployeeCreateView(CrudCreateView):
    cv_viewset = employee_viewset
    form_class = EmployeeForm


class EmployeeUpdateView(CrudUpdateView):
    cv_viewset = employee_viewset
    form_class = EmployeeForm


class EmployeeDeleteView(CrudDeleteView):
    cv_viewset = employee_viewset

    def cv_check_delete_protection(self):
        if self.object.productivity_goals.exists():
            return [
                "This employee cannot be deleted because they have productivity goals."
            ]
        return []


employment_type_viewset = ViewSet(
    model=EmploymentType,
    name="employment_type",
    prefix="employment-types",
)


class EmploymentTypeListView(CrudListView):
    cv_viewset = employment_type_viewset
    table_class = EmploymentTypeTable
    filterset_class = EmploymentTypeFilter


class EmploymentTypeDetailView(CrudDetailView):
    cv_viewset = employment_type_viewset


class EmploymentTypeCreateView(CrudCreateView):
    cv_viewset = employment_type_viewset
    form_class = EmploymentTypeForm


class EmploymentTypeUpdateView(CrudUpdateView):
    cv_viewset = employment_type_viewset
    form_class = EmploymentTypeForm


class EmploymentTypeDeleteView(CrudDeleteView):
    cv_viewset = employment_type_viewset

    def cv_check_delete_protection(self):
        if self.object.productivity_goals.exists():
            return [
                "This employment type cannot be deleted because it has productivity goals."
            ]
        return []


productivity_goal_viewset = ViewSet(
    model=ProductivityGoal,
    name="productivity_goal",
    prefix="productivity-goals",
)


class ProductivityGoalListView(CrudListView):
    cv_viewset = productivity_goal_viewset
    table_class = ProductivityGoalTable
    filterset_class = ProductivityGoalFilter


class ProductivityGoalDetailView(CrudDetailView):
    cv_viewset = productivity_goal_viewset


class ProductivityGoalCreateView(CrudCreateView):
    cv_viewset = productivity_goal_viewset
    form_class = ProductivityGoalForm


class ProductivityGoalUpdateView(CrudUpdateView):
    cv_viewset = productivity_goal_viewset
    form_class = ProductivityGoalForm


class ProductivityGoalDeleteView(CrudDeleteView):
    cv_viewset = productivity_goal_viewset
