from flask import Flask, jsonify, request
import json
import uuid

obj = Flask(__name__)

@obj.route('/v1/users', methods=['GET'])     # Endpoint to retrieve all users from the database.
def Users():
    with open('database.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@obj.route('/v1/users/ids', methods=['GET'])     # Endpoint to retrieve a user by their ID.
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

@obj.route('/v1/users/teams', methods=['GET'])       # Endpoint to retrieve users by their team code.
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
    
@obj.route('/v1/users/new_users', methods=["POST"])      # Endpoint to create a new user.
def new_user():
    # Retrieve JSON data from the request
    data = request.get_json()

    # Define the required fields for creating a new user
    required_fields = ["name", "age", "team"]
    
    # Initialize a list to track any missing fields
    missing_fields = []
    
    # Check for each required field in the incoming data
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)  # Add missing fields to the list
    
    # If there are any missing fields, return an error message
    if missing_fields:
        # Create a string of missing fields for the error message
        missing_fields_str = ", ".join(missing_fields)
        return jsonify({
            "error": f"Cannot create user as following attributes are missing: {missing_fields_str}"
        })
    
    # Extract user details from the data (known as request body)
    name = data["name"]
    age = int(data["age"])
    team = data["team"]
    
    # Generate a unique user ID using UUID
    user_id = str(uuid.uuid4())
    
    # Create a new user dictionary with the extracted details
    new_user = {
        "id": user_id,
        "name": name,
        "age": age,
        "team": team
    }

    try:
        # Attempt to read existing user data
        with open('database.json', 'r') as file:
            existing_data = json.load(file)  # Load existing data
        
    except (json.JSONDecodeError, FileNotFoundError):
        existing_data = {"users": []}
    
    # Append the new user to the existing users list
    existing_data["users"].append(new_user)
        
    # Write the updated user data back 
    with open('database.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

    # Return a success message
    return f"User added successfully with id {user_id}"

@obj.route('/v1/users/update_users', methods=["PUT"])      # Endpoint to update an existing user.
def update_user():
    # Retrieve JSON data from the request
    data = request.get_json()
    
    # Get the user ID from the query parameters
    user_id = request.args.get('id')

    # "get" used as then no need for all inputs necessary (known as request body)
    name = data.get("name")
    age = data.get("age")
    team = data.get("team")

    # Open file to read existing user data
    with open('database.json', 'r') as file:
        existing_data = json.load(file) 
    
    # Access the list of users 
    users = existing_data["users"]

    # Iterate through the list of users to find the one to update
    for user in users:
        if user["id"] == user_id:  # Check if the current user's ID matches the provided user ID
            # Update user details if provided in the incoming data
            if "name" in data:
                user["name"] = data["name"]  
            if "age" in data:
                user["age"] = data["age"]
            if "team" in data:
                user["team"] = data["team"] 
            break  

    else:
        return "User not found"

    # Write the updated user data back to file
    with open('database.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

    # Return a success message
    return "User updated successfully"

@obj.route('/v1/users/delete_users', methods=["DELETE"])
def delete_user():
    # Retrieve the user ID from the query parameters of the request
    user_id = request.args.get("id")
    
    # Open file to read existing user data
    with open("database.json", "r") as file:
        existing_data = json.load(file)

    # Access the list of users from the loaded data
    users = existing_data["users"]

    # Initialize an empty list to hold users that will remain after deletion
    updated_users = []

    # Iterate through the list of users to find users that do not match the user_id
    for user in users:
        if (user["id"] != user_id):  
            updated_users.append(user) 

    # Check if any users were removed by comparing lengths of lists
    if len(updated_users) == len(users):
        return "User Not Found"
    
    # Step 6: Update the existing data with the new list of users
    existing_data["users"] = updated_users

    # Step 7: Write the updated user data back to file
    with open("database.json", "w") as file:
        json.dump(existing_data, file, indent=4)  

    # Step 8: Return a success message 
    return f"User Successfully Deleted with id {user_id}"

if __name__ == "__main__":
    obj.run(debug=True)