from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

app = FastAPI(title="Todo List API")

# -------------------------------
# GLOBAL VARIABLES & UTILITIES
# -------------------------------
task_id_counter = 1  # Renamed from 'id' to avoid shadowing built-in 'id()'


def generate_next_id():
    """Generate unique task IDs incrementally."""
    global task_id_counter
    task_id_counter += 1
    return task_id_counter


# -------------------------------
# MODELS (Schemas)
# -------------------------------
class TaskCreate(BaseModel):
    title: str
    description: str


class Task(TaskCreate):
    id: int
    created_at: datetime
    updated_at: datetime
    is_completed: bool = False


class TaskUpdate(BaseModel):
    id: int
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None


# -------------------------------
# IN-MEMORY DATABASE CLASS
# -------------------------------
class Database:
    def __init__(self):
        self._tasks: List[Task] = []

    def add(self, task: Task):
        self._tasks.append(task)

    def get_tasks(self) -> List[Task]:
        return self._tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None


# Create single in-memory DB instance
db = Database()


# -------------------------------
# ENDPOINTS
# -------------------------------

@app.get("/")
def index():
    return {"message": "Welcome to the Todo App"}


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    """Create a new task."""
    global task_id_counter

    if not task.title or not task.description:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Both title and description are required."
        )

    new_task = Task(
        id=task_id_counter,
        title=task.title,
        description=task.description,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        is_completed=False
    )

    db.add(new_task)
    generate_next_id()  # increment ID for next task

    return {
        "success": True,
        "message": "Task created successfully",
        "data": new_task
    }


@app.get("/tasks", response_model=List[Task])
def get_all_tasks():
    """Retrieve all tasks."""
    return db.get_tasks()


@app.patch("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def partial_update(task_id: int, update_data: TaskUpdate):
    """Update a task partially."""
    task = db.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if not update_data.title and not update_data.description and update_data.is_completed is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="At least one field must be provided for update."
        )

    # Update the provided fields
    if update_data.title is not None:
        task.title = update_data.title

    if update_data.description is not None:
        task.description = update_data.description

    if update_data.is_completed is not None:
        task.is_completed = update_data.is_completed

    task.updated_at = datetime.utcnow()

    return {"success": True, "message": "Task updated successfully", "data": task}
