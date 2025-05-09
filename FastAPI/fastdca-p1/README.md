# 🚀 Hello FastAPI – Getting Started with Modern Web APIs

This is a basic FastAPI project created as part of the Panaverse DAO's [Learn Agentic AI](https://github.com/panaversity/learn-agentic-ai) initiative.

It demonstrates how to:

- Create a FastAPI app
- Define simple GET endpoints
- Run the app using `uv` and `uvicorn`
- Access Swagger docs for testing

---

## 🛠️ Installation & Setup

### 1. Create and activate virtual environment using `uv`

```bash
uv init fastdca-p1
cd fastdca-p1
uv venv
.venv\Scripts\activate  # For Windows

2. Install dependencies
bash
Copy
Edit
uv add "fastapi[standard]"
uv add --dev pytest pytest-asyncio
▶️ Running the App
bash
Copy
Edit
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Your API will now be live at:

🌐 http://localhost:8000 – Root endpoint

📘 http://localhost:8000/docs – Swagger API documentation

📗 http://localhost:8000/redoc – ReDoc documentation

📄 API Endpoints
GET /
Returns a welcome message:

json
Copy
Edit
{
  "Hello": "World"
}
GET /items/{item_id}
Returns an item ID and optional query string:

Example: /items/42?q=test

json
Copy
Edit
{
  "item_id": 42,
  "q": "test"
}
✅ Project Structure
bash
Copy
Edit
fastdca-p1/
│
├── main.py           # Main FastAPI app
├── .venv/            # Virtual environment
└── README.md         # You're reading it now!
🤝 Credits
This app was created by Tehmina Naz as part of the Panaverse FastAPI learning track powered by the Governor IT Initiative.