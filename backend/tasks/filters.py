# Import django_filters library
# This helps us add filtering functionality to our API
import django_filters

# Import the Task model
from .models import Task


# Create a filter class for Task model
# This class defines how tasks can be filtered
class TaskFilter(django_filters.FilterSet):

    # Custom filter: return tasks with due_date
    # less than or equal to the given date
    # Example: ?due_before=2026-12-31T00:00:00
    due_before = django_filters.DateTimeFilter(
        field_name="due_date",   # Model field to filter
        lookup_expr="lte"        # lte = less than or equal
    )

    # Custom filter: return tasks with due_date
    # greater than or equal to the given date
    # Example: ?due_after=2026-01-01T00:00:00
    due_after = django_filters.DateTimeFilter(
        field_name="due_date",   # Model field to filter
        lookup_expr="gte"        # gte = greater than or equal
    )

    # Meta class connects this filter to the Task model
    class Meta:
        model = Task  # Apply filters on Task model

        # These fields allow direct filtering like:
        # ?status=pending
        # ?priority=high
        fields = ["status", "priority"]
