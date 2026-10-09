from django import forms

from .models import Employee, EmploymentType, ProductivityGoal


class TablerModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        custom_widgets = self._meta.widgets or {}
        for name, field in self.fields.items():
            widget = field.widget
            if isinstance(widget, forms.CheckboxInput):
                css_class = "form-check-input"
            elif isinstance(widget, forms.Select):
                css_class = "form-select"
            else:
                css_class = "form-control"
            widget.attrs.setdefault("class", css_class)

            if isinstance(widget, forms.Textarea):
                # Django supplies 10 rows even when no widget is configured.
                if name not in custom_widgets and name not in self.declared_fields:
                    widget.attrs.pop("rows", None)
                widget.attrs.setdefault("rows", 3)

            if isinstance(widget, forms.DateInput):
                if widget.input_type == "text":
                    widget.input_type = "date"
                if widget.format is None:
                    widget.format = "%Y-%m-%d"


class EmployeeForm(TablerModelForm):
    class Meta:
        model = Employee
        fields = [
            "first_name",
            "last_name",
            "email",
            "is_active",
        ]


class EmploymentTypeForm(TablerModelForm):
    class Meta:
        model = EmploymentType
        fields = [
            "code",
            "name",
            "description",
            "default_minimum_hours",
            "notes",
            "is_active",
        ]


class ProductivityGoalForm(TablerModelForm):
    class Meta:
        model = ProductivityGoal
        fields = [
            "employee",
            "employment_type",
            "minimum_hours",
            "effective_from",
            "effective_to",
            "notes",
        ]
