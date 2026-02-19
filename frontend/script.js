const API_URL = "http://127.0.0.1:8000/tasks/";

async function loadTasks() {
    const response = await fetch(API_URL);
    const tasks = await response.json();
    displayTasks(tasks);
}

async function filterTasks(status) {
    const response = await fetch(`${API_URL}?status=${status}`);
    const tasks = await response.json();
    displayTasks(tasks);
}

async function createTask() {
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    const priority = document.getElementById("priority").value;

    await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title,
            description,
            priority
        })
    });

    loadTasks();
}

async function deleteTask(id) {
    await fetch(`${API_URL}${id}/`, {
        method: "DELETE"
    });
    loadTasks();
}

async function toggleComplete(task) {
    const newStatus = task.status === "pending" ? "completed" : "pending";

    await fetch(`${API_URL}${task.id}/`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            status: newStatus
        })
    });

    loadTasks();
}

function displayTasks(tasks) {
    const container = document.getElementById("task-list");
    container.innerHTML = "";

    tasks.forEach(task => {
        const div = document.createElement("div");
        div.className = "task";

        if (task.status === "completed") {
            div.classList.add("completed");
        }

        div.innerHTML = `
            <strong>${task.title}</strong> (${task.priority})<br>
            ${task.description}<br>
            Status: ${task.status}<br><br>
            <button onclick='toggleComplete(${JSON.stringify(task)})'>Toggle Complete</button>
            <button onclick="deleteTask(${task.id})">Delete</button>
        `;

        container.appendChild(div);
    });
}

loadTasks();
