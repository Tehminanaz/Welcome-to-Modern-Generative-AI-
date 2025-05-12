# FastAPI Dependency Injection – Simple Guide

This project shows how to use **Dependency Injection** in FastAPI using simple examples.  
Dependencies help us **reuse code**, **organize logic**, and **make testing easier**.

---

## ✅ What is a Dependency?

A **dependency** is a function or class that provides some value to your endpoint.  
FastAPI will automatically run this function before your API function runs, and give you the result.

---

## 🤔 Why use Dependencies?

- 🔁 **Reuse code**: Write logic once, use it in many places.
- 🔐 **Authentication**: Check headers or login info easily.
- 📦 **Data access**: Use database logic as a dependency.
- 🧪 **Testing**: Replace dependencies with fake ones during testing.

---

## 🛠️ How to Run This Project

1. Open terminal and run:

```bash
uv init fastdca_assignment
cd fastdca_assignment
uv venv
source .venv/bin/activate
uv add "fastapi[standard]"

Create main.py file and paste the code.

Run the server:

bash
Copy
Edit
uvicorn main:app --reload
📘 What You Will Learn
1. Simple Dependency
This dependency returns a fixed message.

python
Copy
Edit
def simple_dep():
    return {"goal": "Learn Dependency Injection"}
Endpoint:

bash
Copy
Edit
GET /goal
2. Dependency with Query Parameters
This dependency checks username and password from the URL.

python
Copy
Edit
def login_check(username: str = Query(...), password: str = Query(...)):
    if username == "admin" and password == "admin":
        return {"msg": "Welcome admin"}
Endpoint:

pgsql
Copy
Edit
GET /login?username=admin&password=admin
3. Multiple Dependencies
You can use more than one dependency in the same route.

python
Copy
Edit
def plus_one(num: int): return num + 1
def plus_two(num: int): return num + 2
Endpoint:

sql
Copy
Edit
GET /add/5
4. Class-based Dependency
This class simulates database lookup. If ID not found, return 404.

python
Copy
Edit
class GetObjectOr404:
    def __init__(self, model):
        self.model = model

    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=404, detail="Not Found")
        return obj
Endpoint:

bash
Copy
Edit
GET /blog/1
📦 Example Dictionary Data
python
Copy
Edit
blogs = {"1": "AI", "2": "ML", "3": "DL"}
users = {"8": "Ahmed", "9": "Mohammed"}
You can create similar endpoints for users too.

📂 Folder Structure
css
Copy
Edit
fastdca_assignment/
├── main.py
└── README.md
🧠 Final Thoughts
Using dependencies makes your FastAPI app:

Clean and organized

Easier to test

More reusable

👨‍💻 Created For
Panaverse – Learn Agentic AI (FastDCA)

yaml
Copy
Edit
