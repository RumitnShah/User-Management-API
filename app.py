from flask import Flask, jsonify, request
import json

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
    
if __name__ == "__main__":
    obj.run(debug=True)

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
        return jsonify({"Error": "No team with given code found"})
    
if __name__ == "__main__":
    obj.run(debug=True)