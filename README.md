# TODO_APP Documentation
This project is a To-Do Reminder application that exposes RESTful APIs for managing tasks. It is built using Flask and MongoDB


## Feature
Add a new To-Do task.
Display a list of all To-Do tasks.
Edit or delete a particular To-Do task.
Delete all To-Do tasks.

## Tech Stack
Backend: Flask (Python Framework)
Database: MongoDB (NoSQL Database)

## Setup Instructions
### Prerequisites
Install Python: Download Python
Install MongoDB: Download MongoDB
Install virtualenv for virtual environment management (optional but recommended).



## API Endpoints
1. Add a New To-Do Task
URL: /api/todos
Method: POST
Description: Adds a new to-do task to the database.
Request Body (JSON):
json
Copy code
{
    "title": "Task Title",
    "description": "Task Description"
}
Response (JSON):
json
Copy code
{
    "message": "Todo added successfully!",
    "id": "63e1234567890abcd1234567"
}
Example:
bash
Copy code
curl -X POST http://127.0.0.1:5000/api/todos \
-H "Content-Type: application/json" \
-d '{"title": "Learn Flask", "description": "Study the Flask documentation and tutorials."}'
2. Get All To-Do Tasks
URL: /api/todos
Method: GET
Description: Fetches a list of all to-do tasks in the database.
Response (JSON):
json
Copy code
[
    {
        "id": "63e1234567890abcd1234567",
        "title": "Learn Flask",
        "description": "Study the Flask documentation and tutorials."
    },
    {
        "id": "63e1234567890abcd1234568",
        "title": "Build API",
        "description": "Create RESTful APIs using Flask."
    }
]
Example:
bash
Copy code
curl -X GET http://127.0.0.1:5000/api/todos
3. Edit a To-Do Task
URL: /api/todos/<id>
Method: PUT
Description: Edits the details of an existing to-do task.
Request Body (JSON):
json
Copy code
{
    "title": "Updated Task Title",
    "description": "Updated Task Description"
}
Response (JSON):
json
Copy code
{
    "message": "Todo updated successfully!"
}
Example:
bash
Copy code
curl -X PUT http://127.0.0.1:5000/api/todos/63e1234567890abcd1234567 \
-H "Content-Type: application/json" \
-d '{"title": "Complete Flask Tutorial", "description": "Finish Flask learning."}'
4. Delete a To-Do Task
URL: /api/todos/<id>
Method: DELETE
Description: Deletes a specific to-do task based on its ID.
Response (JSON):
json
Copy code
{
    "message": "Todo deleted successfully!"
}
