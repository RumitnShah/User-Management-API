# User Management API

This project is a Flask-based RESTful API for managing user data stored in Firebase Realtime Database. It allows you to create, retrieve, update, and delete user information.

## Features
- Retrieve all users from the database.
- Retrieve a user by their ID.
- Retrieve users by their team code.
- Add a new user to the database.
- Update an existing user's details.
- Delete a user from the database.

## Prerequisites
- Python 3.6 or higher
- Make sure Python is installed on your machine. You can download it from python.org.

## Installation
1. Clone the given Repository

2. Set Up a Virtual Environment (recommended)
```bash
python -m venv venv
```
3. Activate Virtual Environment 
```bash
On Windows: venv\Scripts\activate
On macOS: source venv/bin/activate
```
4. Configure the Environment File
- Locate the ```.example.env``` file in the repository.
- Rename it to ```.env```.
- Add the required API keys obtained from the respective database to ```.env``` file.

5. Install Dependencies
```bash
pip install -r requirements.txt
```
6. Run the application

## Testing the API

1. Retrieve All Users
    - Endpoint: ``` https://user-management-api1-7c09c950be6a.herokuapp.com/v1/users ```
    - Method: GET

2. Retrieve User by ID
    - Endpoint: ``` https://user-management-api1-7c09c950be6a.herokuapp.com/v1/users/ids?id=<user_id> ```
    - Method: GET

3. Retrieve Users by Team Code
    - Endpoint: ``` https://user-management-api1-7c09c950be6a.herokuapp.com/v1/users/teams?team=<team_code> ```
    - Method: GET

4. Add a New User
    - Endpoint: ``` https://user-management-api1-7c09c950be6a.herokuapp.com/v1/users/new_users ```
    - Method: POST

5. Update an Existing User
    - Endpoint: ``` https://user-management-api1-7c09c950be6a.herokuapp.com/v1/users/update_users?id=<user_id> ```
    - Method: PUT

6. Delete a User
    - Endpoint: ``` https://user-management-api1-7c09c950be6a.herokuapp.com/v1/users/delete_users?id=<user_id> ```
    - Method: DELETE

## Note
- Write in JSON Body if using any API testing platform
- Example JSON Format                                                                                                        
  <img width="116" alt="api" src="https://github.com/user-attachments/assets/5c9475e9-b8c6-457e-947e-c3e3df60e9e8" />

