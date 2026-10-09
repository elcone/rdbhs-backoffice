from crud_views.lib.views import (
    CreateViewPermissionRequired,
    DeleteViewPermissionRequired,
    DetailViewPermissionRequired,
    ListViewPermissionRequired,
    ListViewTableFilterMixin,
    ListViewTableMixin,
    MessageMixin,
    UpdateViewPermissionRequired,
)
from crud_views.lib.viewset import ViewSet

from .filters import EmployeeFilter, EmploymentTypeFilter, ProductivityGoalFilter
from .forms import EmployeeForm, EmploymentTypeForm, ProductivityGoalForm
from .models import Employee, EmploymentType, ProductivityGoal
from .tables import EmployeeTable, EmploymentTypeTable, ProductivityGoalTable

employee_viewset = ViewSet(
    model=Employee,
    name="employee",
    prefix="employees",
)


class EmployeeListView(
    ListViewTableMixin, ListViewTableFilterMixin, ListViewPermissionRequired
):
    cv_viewset = employee_viewset
    table_class = EmployeeTable
    filterset_class = EmployeeFilter
    paginate_by = 20
    cv_filter_persistence = False


class EmployeeDetailView(DetailViewPermissionRequired):
    cv_viewset = employee_viewset
    cv_path = ""
    template_name = "core/employee/detail.html"


class EmployeeCreateView(MessageMixin, CreateViewPermissionRequired):
    cv_viewset = employee_viewset
    cv_path = "add"
    form_class = EmployeeForm


class EmployeeUpdateView(MessageMixin, UpdateViewPermissionRequired):
    cv_viewset = employee_viewset
    cv_path = "edit"
    form_class = EmployeeForm


class EmployeeDeleteView(MessageMixin, DeleteViewPermissionRequired):
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


class EmploymentTypeListView(
    ListViewTableMixin, ListViewTableFilterMixin, ListViewPermissionRequired
):
    cv_viewset = employment_type_viewset
    table_class = EmploymentTypeTable
    filterset_class = EmploymentTypeFilter
    paginate_by = 20
    cv_filter_persistence = False


class EmploymentTypeDetailView(DetailViewPermissionRequired):
    cv_viewset = employment_type_viewset
    cv_path = ""


class EmploymentTypeCreateView(MessageMixin, CreateViewPermissionRequired):
    cv_viewset = employment_type_viewset
    cv_path = "add"
    form_class = EmploymentTypeForm


class EmploymentTypeUpdateView(MessageMixin, UpdateViewPermissionRequired):
    cv_viewset = employment_type_viewset
    cv_path = "edit"
    form_class = EmploymentTypeForm


class EmploymentTypeDeleteView(MessageMixin, DeleteViewPermissionRequired):
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


class ProductivityGoalListView(
    ListViewTableMixin, ListViewTableFilterMixin, ListViewPermissionRequired
):
    cv_viewset = productivity_goal_viewset
    table_class = ProductivityGoalTable
    filterset_class = ProductivityGoalFilter
    paginate_by = 20
    cv_filter_persistence = False


class ProductivityGoalDetailView(DetailViewPermissionRequired):
    cv_viewset = productivity_goal_viewset
    cv_path = ""


class ProductivityGoalCreateView(MessageMixin, CreateViewPermissionRequired):
    cv_viewset = productivity_goal_viewset
    cv_path = "add"
    form_class = ProductivityGoalForm


class ProductivityGoalUpdateView(MessageMixin, UpdateViewPermissionRequired):
    cv_viewset = productivity_goal_viewset
    cv_path = "edit"
    form_class = ProductivityGoalForm


class ProductivityGoalDeleteView(MessageMixin, DeleteViewPermissionRequired):
    cv_viewset = productivity_goal_viewset
