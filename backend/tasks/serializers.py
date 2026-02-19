# Import serializers from Django REST Framework
# Used to convert model data <-> JSON
from rest_framework import serializers

# Import timezone to compare dates
from django.utils import timezone

# Import Task model
from .models import Task


# Create serializer for Task model
# ModelSerializer automatically creates fields based on model
class TaskSerializer(serializers.ModelSerializer):

    # Meta class connects serializer with model
    class Meta:
        model = Task              # Use Task model
        fields = "__all__"        # Include all model fields
        read_only_fields = ("id", "created_at")  
        # These fields cannot be modified by user
        # id is auto-generated
        # created_at is automatically set when task is created

    # Custom Validation for due_date
    
    def validate_due_date(self, value):
        """
        This function automatically runs when user sends due_date.
        It checks if the date is in the past.
        """

        # If due_date exists and is earlier than current time
        if value and value < timezone.now():
            raise serializers.ValidationError(
                "Due date cannot be in the past."
            )

        return value  # Return valid value


    # Custom Validation for title
   
    def validate_title(self, value):
        """
        This function checks that title is not empty
        or just spaces.
        """

        # Remove spaces and check length
        if len(value.strip()) == 0:
            raise serializers.ValidationError(
                "Title cannot be empty."
            )

        return value  # Return valid value
