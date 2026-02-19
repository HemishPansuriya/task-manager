# Import DefaultRouter from Django REST Framework
# Router automatically creates URL patterns for ViewSets
from rest_framework.routers import DefaultRouter

# Import TaskViewSet from views.py
from .views import TaskViewSet


# Create router object
# Router helps generate URLs automatically
router = DefaultRouter()

# Register TaskViewSet with the router
# "tasks" → this will be the URL path (e.g., /tasks/)
# TaskViewSet → the view handling the requests
# basename="task" → base name for URL reversing
router.register(r"tasks", TaskViewSet, basename="task")


# This automatically creates all required API endpoints
urlpatterns = router.urls
