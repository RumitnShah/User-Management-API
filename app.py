from flask import Flask, jsonify, request
import json
import uuid

obj = Flask(__name__)

@obj.route('/v1/users', methods=['GET'])     #To get all the users.
def Users():
    with open('database.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@obj.route('/v1/users/ids', methods=['GET'])     # To get users with specific id only
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
    else:
            return jsonify({"Error" : f"User with {user_id} does not exist"})

@obj.route('/v1/users/teams', methods=['GET'])       #To get users with same team code
def user_team():
    user_team = request.args.get('team')
    
    if not user_team:
        return jsonify({"error": "No user team provided"})

    with open('database.json', 'r') as file:
        data = json.load(file)

    users = data.get("users", [])

    same_code_team = []

    for user in users:
        if user["team"] == user_team:
            same_code_team.append({
                                        "id": user["id"],
                                        "name": user["name"],
                                        "age": user["age"],
                                        "team": user["team"]
                                    })
    if same_code_team:
        return jsonify(same_code_team)
    
    else:
        return jsonify({"Error": f"No team with {user_team} code found"})
    
@obj.route('/v1/users/new_users', methods=["POST"])      #To add new user
def new_user():
    data = request.get_json()

    required_fields = ["name", "age", "team"]
    
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
    
    if missing_fields:
        missing_fields_str = ", ".join(missing_fields)
        return jsonify({
            "error": f"Cannot create user as following attributes are missing: {missing_fields_str}"
        })
    
    name = data["name"]
    age = data["age"]
    team = data["team"]
    
    user_id = str(uuid.uuid4())
    new_user = {
        "id": user_id,
        "name": name,
        "age": age,
        "team": team
    }

    try:
        with open('database.json', 'r') as file:
            existing_data = json.load(file)
        
    except (json.JSONDecodeError, FileNotFoundError):
        existing_data = {"users": []}
    
    existing_data["users"].append(new_user)
        
    with open('database.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

    return "User added succesfully"

if __name__ == "__main__":
    obj.run(debug=True)