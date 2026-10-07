from django.db import models


class EmploymentType(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    default_minimum_hours = models.PositiveIntegerField()
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "employment type"
        verbose_name_plural = "employment types"

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "employee"
        verbose_name_plural = "employees"

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class ProductivityGoalQuerySet(models.QuerySet):
    def with_related(self):
        return self.select_related("employee", "employment_type")


class ProductivityGoalManager(models.Manager.from_queryset(ProductivityGoalQuerySet)):
    def get_queryset(self):
        return super().get_queryset().with_related()


class ProductivityGoal(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.PROTECT, related_name="productivity_goals"
    )
    employment_type = models.ForeignKey(
        EmploymentType, on_delete=models.PROTECT, related_name="productivity_goals"
    )
    minimum_hours = models.PositiveIntegerField()
    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductivityGoalManager()

    class Meta:
        ordering = ["employee__last_name", "employee__first_name", "-effective_from"]
        verbose_name = "productivity goal"
        verbose_name_plural = "productivity goals"
        constraints = [
            models.CheckConstraint(
                condition=models.Q(effective_to__isnull=True)
                | models.Q(effective_to__gte=models.F("effective_from")),
                name="productivity_goal_valid_effective_dates",
            ),
        ]

    def __str__(self):
        return (
            f"{self.employee} - {self.minimum_hours} hours from {self.effective_from}"
        )
