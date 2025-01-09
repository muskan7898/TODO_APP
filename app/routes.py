from flask import Blueprint, request, jsonify
from bson import ObjectId
from main import mongo

todo_bp = Blueprint('todo', __name__)

''' 
Add a New To-Do Task
'''
@todo_bp.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    todo_id = mongo.db.todos.insert_one({
        "title": data['title'],
        "description": data['description']
    }).inserted_id
    return jsonify({"message": "Todo added successfully!", "id": str(todo_id)}), 201


'''
Get All To-Do Tasks
'''
@todo_bp.route('/todos', methods=['GET'])
def get_todos():
    print("REQUEST TO GET ALL TODOS")
    todos = mongo.db.todos.find()
    result = [{"id": str(todo["_id"]), "title": todo["title"], "description": todo["description"]} for todo in todos]
    return jsonify(result)


''' 
Update todo by id
'''
@todo_bp.route('/todos/<string:id>', methods=['PUT'])
def update_todo(id):
    try:
        ''' Validate ObjectId'''
        if not ObjectId.is_valid(id):
            return jsonify({"error": "Invalid ID format"}), 400

        '''Parse JSON data from request'''
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        '''Validate required fields'''
        title = data.get("title")
        description = data.get("description")
        if not title or not description:
            return jsonify({"error": "Title and description are required"}), 400

        '''Update the To-Do item in the database'''
        result = mongo.db.todos.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"title": title, "description": description}}
        )

        '''Check if the document was found and updated'''
        if result.matched_count == 0:
            return jsonify({"error": "Todo not found"}), 404

        
        ''' Fetch the updated document'''
        updated_todo = mongo.db.todos.find_one({"_id": ObjectId(id)})
        updated_todo["_id"] = str(updated_todo["_id"])

        return jsonify({"message": "Todo updated successfully!", "todo": updated_todo}), 200

    except PyMongoError as e:
        # Handle database-related errors
        return jsonify({"error": f"Database error: {str(e)}"}), 500

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

'''
Delete a To-Do Task
'''
@todo_bp.route('/todos/<string:id>', methods=['DELETE'])
def delete_todo(id):
    mongo.db.todos.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Todo deleted successfully!"})

'''
Delete All To-Do Tasks
'''
@todo_bp.route('/todos', methods=['DELETE'])
def delete_all_todos():
    mongo.db.todos.delete_many({})
    return jsonify({"message": "All Todos deleted successfully!"})
