Task Tracker API Assignment Documentation
Project Overview
The goal of this assignment was to implement a Task Tracker API using FastAPI, with an emphasis on managing Users and their Tasks. The key aspects of the API include the creation, retrieval, and management of users and tasks. The API uses Pydantic models for validation, FastAPI for handling HTTP requests, and Python dictionaries to store data.

Technologies Used
FastAPI: A modern web framework for building APIs with Python.

Pydantic: A data validation library used to define and validate request and response data schemas.

Uvicorn: ASGI server to run the FastAPI app.

Python: The primary programming language for implementing the API.

Features Implemented
User Management:

Create User: A POST endpoint to create a new user with a validated username and email.

Retrieve User: A GET endpoint to retrieve user details by user ID.

Task Management:

Create Task: A POST endpoint to create a task, linked to a user.

Retrieve Task: A GET endpoint to retrieve a task by task ID.

Update Task: A PUT endpoint to update the status of a task (pending, in_progress, completed).

List Tasks for a User: A GET endpoint to list all tasks associated with a specific user.

Steps Taken and Reasoning
1. Setup FastAPI Project:
We initialized the FastAPI project using uvicorn.

Created a simple "Hello World" endpoint as a first step to verify that the FastAPI server was set up correctly.

2. Creating Pydantic Models:
User Models:

UserCreate: Used to accept input data for creating users with email and username validation. We used EmailStr for email validation and constr for enforcing length constraints on the username.

UserRead: Represents the user data returned after creation, including an id.

Task Models:

TaskBase: The base class for tasks, which includes fields for title, description, due date, and status. The due_date field has a validation method to ensure that the due date is not in the past, and the status field is validated to ensure it's one of the allowed values (pending, in_progress, completed).

TaskCreate: Inherits from TaskBase and adds a user_id field to associate a task with a user.

Task: Represents a task, including the id and user_id.

3. Endpoints Implementation:
POST /users/: Creates a user by accepting a UserCreate payload and returning a UserRead response. A global counter is used to auto-increment user IDs.

GET /users/{user_id}: Fetches user details by user ID. If the user does not exist, it returns a 404 error.

POST /tasks/: Creates a task and associates it with a user. It checks if the user exists before creating the task and uses a global task counter to auto-increment task IDs.

GET /tasks/{task_id}: Fetches task details by task ID. If the task does not exist, it returns a 404 error.

PUT /tasks/{task_id}: Updates the status of an existing task. It checks that the status is one of the allowed values.

GET /users/{user_id}/tasks: Lists all tasks associated with a user. It ensures the user exists before fetching the tasks.

4. Data Storage:
Users and Tasks data were stored in two global dictionaries: users_db and tasks_db. These act as in-memory databases for this simple application, simulating storage.

5. Error Handling:
Custom error messages are provided for common cases such as invalid input (e.g., invalid status) or non-existent users/tasks.

Used HTTPException from FastAPI to return detailed error messages and status codes.

Challenges Faced
Pydantic V2 Migration: During development, Pydantic's @validator function was deprecated, and we needed to migrate to @field_validator for field-level validation. This change caused some confusion, but it was quickly resolved by following the new Pydantic V2 syntax.

In-Memory Data Storage: Using in-memory dictionaries (users_db and tasks_db) for data storage meant that the data would be lost each time the server is restarted. This was fine for the purpose of this assignment but would need to be replaced by a real database for production use.

Testing the API
Swagger UI: FastAPI provides an interactive Swagger UI at http://localhost:8000/docs, where all the API endpoints can be tested easily.

Postman: The API was also tested using Postman by sending requests to endpoints and verifying the responses.

Conclusion
The Task Tracker API was successfully implemented using FastAPI, Pydantic, and simple in-memory storage.

The API allows users to create, retrieve, and manage tasks while ensuring data integrity and validation using Pydantic models.

The use of FastAPI’s automatic documentation and validation made the development process fast and efficient.

