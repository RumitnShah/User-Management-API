# User Management API

This project is a Flask-based RESTful API for managing user data stored in Firebase Realtime Database. It allows you to create, retrieve, update, and delete user information.

# Features
- Retrieve all users from the database.
- Retrieve a user by their ID.
- Retrieve users by their team code.
- Add a new user to the database.
- Update an existing user's details.
- Delete a user from the database.

# Prerequisites
- Python 3.6 or higher
- Make sure Python is installed on your machine. You can download it from python.org.

# Installation
1. Clone the given Repository

2. Set Up a Virtual Environment (recommended)
'python -m venv venv'
On Windows: 'venv\Scripts\activate'

3. Install Dependencies
'pip install -r requirements.txt'

4. Run the application

# Testing the API

1. Retrieve All Users
    - Endpoint: /v1/users
    - Method: GET

2. Retrieve User by ID
    - Endpoint: https://user-management-api1-7c09c950be6a.herokuapp.com/v1/users/ids?id=<user_id>
    - Method: GET

3. Retrieve Users by Team Code
    - Endpoint: https://user-management-api1-7c09c950be6a.herokuapp.com/v1/users/teams?team=<team_code>
    - Method: GET

4. Add a New User
    - Endpoint: https://user-management-api1-7c09c950be6a.herokuapp.com/v1/users/new_users?name=<name>&age=<age>&team=<team>
    - Method: POST

5. Update an Existing User
    - Endpoint: https://user-management-api1-7c09c950be6a.herokuapp.com/v1/users/update_users?id=<user_id>&name=<name>&age=<age>&team=<team>
    - Method: PUT

6. Delete a User
    - Endpoint: https://user-management-api1-7c09c950be6a.herokuapp.com/v1/users/delete_users?id=<user_id>
    - Method: DELETE

# Note
- Write in JSON Body if using any API testing platform
Example JSON Format
{
    "name" : "xyz"
    "age" : 20
    "team" : "code"
}