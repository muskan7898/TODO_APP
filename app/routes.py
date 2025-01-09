from flask import Blueprint, request, jsonify
from app.database import mongo
from bson import ObjectId

todo_bp = Blueprint('todo', __name__)

# Add a New To-Do Task
@todo_bp.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    todo_id = mongo.db.todos.insert_one({
        "title": data['title'],
        "description": data['description']
    }).inserted_id
    return jsonify({"message": "Todo added successfully!", "id": str(todo_id)}), 201

# Get All To-Do Tasks
@todo_bp.route('/todos', methods=['GET'])
def get_todos():
    todos = mongo.db.todos.find()
    result = [{"id": str(todo["_id"]), "title": todo["title"], "description": todo["description"]} for todo in todos]
    return jsonify(result)

# Update a To-Do Task
@todo_bp.route('/todos/<string:id>', methods=['PUT'])
def update_todo(id):
    data = request.get_json()
    mongo.db.todos.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"title": data.get("title"), "description": data.get("description")}}
    )
    return jsonify({"message": "Todo updated successfully!"})

# Delete a To-Do Task
@todo_bp.route('/todos/<string:id>', methods=['DELETE'])
def delete_todo(id):
    mongo.db.todos.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Todo deleted successfully!"})

# Delete All To-Do Tasks
@todo_bp.route('/todos', methods=['DELETE'])
def delete_all_todos():
    mongo.db.todos.delete_many({})
    return jsonify({"message": "All Todos deleted successfully!"})
