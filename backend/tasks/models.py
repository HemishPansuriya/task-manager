# Import models module from Django
# This is used to create database tables
from django.db import models

# Import timezone (used if we need current time)
from django.utils import timezone


# Create Task model (this creates a database table called Task)
class Task(models.Model):

 
    # Status Choices (Dropdown options)
   
    # TextChoices is used to define fixed options
    # Only these values can be saved in the database
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"        # Stored value , Display value
        COMPLETED = "completed", "Completed"

    
    # Priority Choices
    
    class Priority(models.TextChoices):
        LOW = "low", "Low"
        MEDIUM = "medium", "Medium"
        HIGH = "high", "High"

    
    # Model Fields (Table Columns)
    

    # Title of the task (maximum 255 characters)
    title = models.CharField(max_length=255)

    # Description of task
    # blank=True means this field is optional in forms
    description = models.TextField(blank=True)

    # Status field (only accepts values from Status choices)
    # Default value is "pending"
    status = models.CharField(
        max_length=20,
        choices=Status.choices,      # Restricts values
        default=Status.PENDING      # Default value
    )

    # Priority field (only accepts values from Priority choices)
    # Default value is "medium"
    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )

    # Automatically stores date & time when task is created
    created_at = models.DateTimeField(auto_now_add=True)

    # Due date for task
    # null=True → allows NULL in database
    # blank=True → allows empty in forms
    due_date = models.DateTimeField(null=True, blank=True)

    # This controls how the object is displayed in Django admin & shell
    def __str__(self):
        return self.title
