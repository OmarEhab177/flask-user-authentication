from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary to store user credentials
users = {}


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({'message': 'Username already exists'}), 400

    users[username] = password
    return jsonify({'message': 'User registered successfully'})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username not in users or users[username] != password:
        return jsonify({'message': 'Access denied'}), 401

    return jsonify({'message': 'Access granted'})


if __name__ == '__main__':
    app.run()
