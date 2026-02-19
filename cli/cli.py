# Import Typer for building CLI applications
import typer

# Import requests to send HTTP requests to the Django API
import requests

# Import rich print for styled/colored terminal output
from rich import print


# Base URL of your Django Task API
API_URL = "http://127.0.0.1:8000/tasks/"


# Create Typer application instance
app = typer.Typer()


# CREATE TASK COMMAND

@app.command()
def create(title: str, description: str = "", priority: str = "medium"):
    """
    Create a new task using API.
    Example:
    python cli.py create "Buy Milk" --priority high
    """

    # Data to send to API
    payload = {
        "title": title,
        "description": description,
        "priority": priority
    }

    # Send POST request to create task
    response = requests.post(API_URL, json=payload)

    # Print API response
    print(response.json())


# LIST TASKS COMMAND

@app.command()
def list(status: str = None, priority: str = None):
    """
    List tasks from API.
    Optional filters:
    --status pending
    --priority high
    """

    # Dictionary to store filter parameters
    params = {}

    # Add filters only if provided
    if status:
        params["status"] = status

    if priority:
        params["priority"] = priority

    # Send GET request with filters
    response = requests.get(API_URL, params=params)

    # Loop through each task and print formatted output
    for task in response.json():
        print(
            f"[bold]{task['id']}[/bold] - "
            f"{task['title']} "
            f"({task['status']}, {task['priority']})"
        )



# MARK TASK AS COMPLETED
@app.command()
def complete(task_id: int):
    """
    Mark a task as complete.
    Example:
    python cli.py complete 1
    """

    # Call custom API endpoint
    response = requests.post(f"{API_URL}{task_id}/mark_complete/")

    # Print server response
    print(response.json())



# DELETE TASK COMMAND

@app.command()
def delete(task_id: int):
    """
    Delete a task by ID.
    Example:
    python cli.py delete 1
    """

    # Send DELETE request
    response = requests.delete(f"{API_URL}{task_id}/")

    # Check if deletion was successful
    if response.status_code == 204:
        print("Task deleted successfully.")
    else:
        print(response.json())


# Run the CLI application
if __name__ == "__main__":
    app()
