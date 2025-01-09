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
Install virtualenv for virtual environment management
pip install Flask flask-pymongo flask-restful pytest
python -m venv venv
venv\Scripts\activate   




## API Endpoints
### Add a New To-Do Task
URL: /api/todos
1.Method: POST
2.Description: Adds a new to-do task to the database.

Request Body (JSON):

{
    "title": "Task Title",
    "description": "Task Description"
}
Response (JSON):

{
    "message": "Todo added successfully!",
    "id": "63e1234567890abcd1234567"
}


### Get All To-Do Tasks
URL: /api/todos
Method: GET
Description: Fetches a list of all to-do tasks in the database.
Response (JSON):
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


### Edit a To-Do Task
#### URL: /api/todos/<id>
#### Method: PUT
#### Description: Edits the details of an existing to-do task.
Request Body (JSON):
{
    "title": "Updated Task Title",
    "description": "Updated Task Description"
}

Response (JSON):

{
    "message": "Todo updated successfully!"
}


### Delete a To-Do Task
#### URL: /api/todos/<id>
#### Method: DELETE
#### Description: Deletes a specific to-do task based on its ID.

Response (JSON):
{
    "message": "Todo deleted successfully!"
}


### Delete All To-Do Tasks
#### URL: /api/todos
#### Method: DELETE
#### Description: Deletes all to-do tasks from the database.

Response (JSON):
{
    "message": "All todos deleted successfully!"
}


## Test cases
pip install pytest
pytest tests/
