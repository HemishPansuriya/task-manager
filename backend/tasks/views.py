# Import ModelViewSet
# ModelViewSet automatically provides:
# list, create, retrieve, update, partial_update, delete
from rest_framework import viewsets

# Used to create custom endpoints (extra actions)
from rest_framework.decorators import action

# Used to return JSON responses
from rest_framework.response import Response

# Used to enable filtering in API
from django_filters.rest_framework import DjangoFilterBackend

# Import Task model
from .models import Task

# Import serializer
from .serializers import TaskSerializer

# Import custom filter class
from .filters import TaskFilter


# Create a ViewSet for Task
# ModelViewSet gives full CRUD functionality automatically
class TaskViewSet(viewsets.ModelViewSet):

    # Get all tasks from database
    # Order by newest first (-created_at)
    queryset = Task.objects.all().order_by("-created_at")

    # Use TaskSerializer to convert model <-> JSON
    serializer_class = TaskSerializer

    # Enable filtering support
    filter_backends = [DjangoFilterBackend]

    # Connect our custom filter class
    filterset_class = TaskFilter


   
    # Custom Action: Mark Complete
  
    @action(detail=True, methods=["post"])
    def mark_complete(self, request, pk=None):
        """
        Custom endpoint:
        POST /tasks/<id>/mark_complete/
        """

        # Get the specific task object by ID
        task = self.get_object()

        # Change status to completed
        task.status = Task.Status.COMPLETED

        # Save changes to database
        task.save()

        # Return JSON response
        return Response({"status": "Task marked as complete"})


   
    # Custom Action: Mark Incomplete
    
    @action(detail=True, methods=["post"])
    def mark_incomplete(self, request, pk=None):
        """
        Custom endpoint:
        POST /tasks/<id>/mark_incomplete/
        """

        # Get task by ID
        task = self.get_object()

        # Change status to pending
        task.status = Task.Status.PENDING

        # Save changes
        task.save()

        # Return response
        return Response({"status": "Task marked as incomplete"})
