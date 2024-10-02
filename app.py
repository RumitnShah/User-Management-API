from flask import Flask, jsonify, request
import json

obj = Flask(__name__)

# @obj.route('/v1/users')
# def Users():
#     with open('database.json', 'r') as file:
#         data = json.load(file)
#     return jsonify(data)

@obj.route('/v1/users')
def user_id():
    user_id = request.args.get('id')
    
    if not user_id:
        return jsonify({"error": "No user ID provided"})

    with open('database.json', 'r') as file:
        data = json.load(file)

    users = data.get("users", [])
    
    for user in users:
        if user["id"] == user_id:
            return jsonify({
                "id": user["id"],
                "name": user["name"],
                "age": user["age"],
                "team": user["team"]
            })
    
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    obj.run(debug=True)