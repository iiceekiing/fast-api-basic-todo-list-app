```markdown
# 📝 FastAPI Todo List App

A simple, beginner-friendly **Todo List API** built with **FastAPI** and **Pydantic**.  
This project demonstrates how to build a basic CRUD (Create, Read, Update, Delete) REST API using FastAPI — one of the fastest and most modern Python frameworks.

---

## 🚀 Features

✅ Create new tasks  
✅ Retrieve all tasks  
✅ Update (partially) a specific task  
✅ Mark tasks as completed  
✅ In-memory database using Python lists  
✅ Auto-generated interactive API docs via Swagger UI  

---

## 🧱 Tech Stack

| Tool | Description |
|------|--------------|
| **FastAPI** | Web framework for building APIs |
| **Pydantic** | Data validation and serialization |
| **Uvicorn** | ASGI server for running FastAPI apps |
| **Python 3.10+** | Core programming language |

---

## 📂 Project Structure

```

fastapi-todo-list/
│
├── main.py            # Main FastAPI application file
├── requirements.txt   # Dependencies list
├── .gitignore         # Ignored files for Git
└── README.md          # Project documentation

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/iiceekiing/fast-api-basic-todo-list-app.git
cd fast-api-basic-todo-list-app
````

### 2️⃣ Create and activate a virtual environment

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` file yet, run:

```bash
pip install fastapi uvicorn
pip freeze > requirements.txt
```

---

## ▶️ Running the App

Run the server using **Uvicorn**:

```bash
uvicorn main:app --reload
```

You’ll see something like:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Now open your browser at:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc UI:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📡 API Endpoints

| Method  | Endpoint           | Description                                                        |
| ------- | ------------------ | ------------------------------------------------------------------ |
| `GET`   | `/`                | Welcome route                                                      |
| `POST`  | `/tasks`           | Create a new task                                                  |
| `GET`   | `/tasks`           | Retrieve all tasks                                                 |
| `PATCH` | `/tasks/{task_id}` | Update an existing task (title, description, or completion status) |

### ✅ Example: Create a Task

**POST** `/tasks`

**Request Body**

```json
{
  "title": "Learn FastAPI",
  "description": "Study FastAPI docs and build a simple project"
}
```

**Response**

```json
{
  "success": true,
  "message": "Task created successfully",
  "data": {
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Study FastAPI docs and build a simple project",
    "is_completed": false,
    "created_at": "2025-10-27T12:00:00Z",
    "updated_at": "2025-10-27T12:00:00Z"
  }
}
```

---

## 🧠 Learning Objectives

By building this mini-project, you will learn:

* How to structure a FastAPI project
* How to create Pydantic models for data validation
* How to perform CRUD operations
* How to design clean and RESTful API routes
* How to test and explore APIs using Swagger UI

---

## 🌟 Future Improvements

🔹 Add Delete Endpoint (`DELETE /tasks/{id}`)
🔹 Add “Mark as Completed” toggle
🔹 Persist tasks in a JSON or SQLite database
🔹 Add user authentication (JWT)
🔹 Deploy API to Render or Vercel

---

## 👨‍💻 Author

**iiceekiing**
💼 Fullstack Software Engineer | Web3 Developer
🔗 [LinkedIn](https://linkedin.com/in/iiceekiing)
🐙 [GitHub](https://github.com/iiceekiing)
🐦 [X (Twitter)](https://x.com/iiceekiing)

---

## 🛡️ License

This project is licensed under the **MIT License** — you’re free to modify and use it for learning or personal projects.

---

> “The best way to learn is by building.” — Keep coding, keep improving! 🚀

```
