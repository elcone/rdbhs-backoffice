from .views import employee_viewset, employment_type_viewset, productivity_goal_viewset

urlpatterns = (
    employee_viewset.urlpatterns
    + employment_type_viewset.urlpatterns
    + productivity_goal_viewset.urlpatterns
)
