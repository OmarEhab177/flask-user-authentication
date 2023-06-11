# Simple User Authentication System with Flask

This is a simple user authentication system implemented using Flask, a lightweight web framework for Python. It provides endpoints for user registration and login.

## Requirements

- Python 3.x
- Flask (install via `pip install flask`)

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/flask-user-authentication.git
cd flask-user-authentication
```

2. Create and activate a virtual environment (optional but recommended):

```
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:

```
python app.py
```

2. Open your web browser and access the following URLs:

- User Registration: http://localhost:5000/register

- User Login: http://localhost:5000/login

3. Using an API testing tool (e.g., Postman), send a POST request to the `/register` endpoint with a JSON payload containing the `username` and `password` fields. Example:

```json
{
  "username": "john_doe",
  "password": "pass123"
}
```

4. If the registration is successful, you will receive a JSON response with the message "User registered successfully".

5. To log in, send a POST request to the `/login` endpoint with the same JSON payload containing the `username` and `password` fields.

6. If the login credentials are correct, you will receive a JSON response with the message "Access granted". Otherwise, you will receive a JSON response with the message "Access denied".

## Note

This is a simplified example meant for learning purposes and should not be used as-is in a production environment. In a real-world scenario, you would need to use secure storage for user credentials, such as a database with hashed passwords.
