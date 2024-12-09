from flask import Flask, jsonify, request
import uuid
import os
from dotenv import load_dotenv
import pyrebase

# Load environment variables from the .env file
load_dotenv()

# Retrieve Firebase configuration from environment variables
firebase_config = {
    "apiKey": os.getenv("apikey"),
    "authDomain": os.getenv("authDomain"),
    "databaseURL": os.getenv("databaseURL"),
    "projectId": os.getenv("projectId"),
    "storageBucket": os.getenv("storageBucket"),
    "messagingSenderId": os.getenv("messagingSenderId"),
    "appId": os.getenv("appId")
}

firebase = pyrebase.initialize_app(firebase_config)
database = firebase.database()

app = Flask(__name__)

@app.route('/v1/users', methods=['GET'])     # Endpoint to retrieve all users from the database.
def Users():
    
    # Fetch all data from the "Users" node in the Firebase Realtime Database
    users_data = database.child("Users").get()

    # Initialize an empty list to store user information
    user_list = []

    # Loop through each user in the retrieved data
    for user in users_data.each():
        # Append each user's key and value as a dictionary to the list
        user_list.append({
            "user_id": user.key(),    # User's unique key
            "user_data": user.val()   # User's data (value)
        })

    # Return the list of user dictionaries as a JSON response
    return jsonify(user_list)


@app.route('/v1/users/ids', methods=['GET'])     # Endpoint to retrieve a user by their ID.
def user_id():
    user_id = request.args.get('id')
    
    if not user_id:
        return jsonify({"error": "No user ID provided"})

    # Fetch all data from the "Users" node in the Firebase Realtime Database
    users_data = database.child("Users").get()

    # Loop through each user in the retrieved data
    for user in users_data.each():
        # Check if the current user's key matches the given user_id ,If a match is found, return the user's data
        if user.key() == user_id:
            return jsonify(user.val())

    # If no match is found after the loop, return an error message
    else:
        return jsonify({"Error": f"User with {user_id} does not exist"})


@app.route('/v1/users/teams', methods=['GET'])       # Endpoint to retrieve users by their team code.
def user_team():
    user_team = request.args.get('team')
    
    if not user_team:
        return jsonify({"error": "No user team provided"})

    # Fetch all user data
    users_data = database.child("Users").get()

    # List to store users in the same team
    same_code_team = []

    # Check each user's team
    for user in users_data.each():
        if user.val()["team"] == user_team:
            same_code_team.append({"user_data": user.val()})  # Add to the list if team matches

    # Return matching team data or an error if no match is found
    if same_code_team:
        return jsonify(same_code_team)
    else:
        return jsonify({"Error": f"No team with {user_team} code found"})

    
@app.route('/v1/users/new_users', methods=["POST"])      # Endpoint to create a new user.
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

    # Add user's data in the "Users" node with the given user_id
    database.child("Users").child(user_id).set(new_user)

    # Return a success message
    return f"User added successfully with id {user_id}"

@app.route('/v1/users/update_users', methods=["PUT"])      # Endpoint to update an existing user.
def update_user():
    # Retrieve JSON data from the request
    data = request.get_json()
    
    # Get the user ID from the query parameters
    user_id = request.args.get('id')

    # "get" used as then no need for all inputs necessary (known as request body)
    name = data.get("name")
    age = data.get("age")
    team = data.get("team")

    # Update user details if provided in the incoming data
    if "name" in data:
        database.child("Users").child(user_id).update({"name" : name})
    if "age" in data:
        database.child("Users").child(user_id).update({"age" : age})
    if "team" in data:
        database.child("Users").child(user_id).update({"team" : team}) 

    # Return a success message
    return "User updated successfully"

@app.route('/v1/users/delete_users', methods=["DELETE"])
def delete_user():
    # Retrieve the user ID from the query parameters of the request
    user_id = request.args.get("id")

    # Fetch all user data from the "Users" node
    users_data = database.child("Users").get()

    # Loop through users to find the matching user_id
    for user in users_data.each():
        if user.key() == user_id:
            # If user is found, delete them from the database
            database.child("Users").child(user_id).remove()
            return "User successfully deleted!"

    # If no user matches, return an error message
    else:
        return jsonify({"Error": f"User Not Found with user id {user_id}"})

if __name__ == "__main__":
    # Get the PORT environment variable from Heroku, with a default of 5000 for local development
    port = int(os.environ.get("PORT", 5000))
    # Bind to all interfaces
    app.run(host="0.0.0.0", port=port)