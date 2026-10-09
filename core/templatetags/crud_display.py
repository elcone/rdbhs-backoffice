from django import template
from django.db import models
from django.utils.text import capfirst

register = template.Library()


@register.simple_tag
def model_label(view):
    return view.cv_viewset.model._meta.verbose_name


@register.simple_tag
def detail_fields(obj):
    """Display concrete fields without requiring per-model detail markup."""
    fields = []
    for field in obj._meta.fields:
        if field.primary_key:
            continue
        value = getattr(obj, field.name)
        if isinstance(field, models.BooleanField) and value is not None:
            value = "Yes" if value else "No"
        elif field.choices:
            value = getattr(obj, f"get_{field.name}_display")()
        fields.append((capfirst(field.verbose_name), value))
    return fields
