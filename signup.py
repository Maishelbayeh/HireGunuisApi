from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database
users = []

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Validation
    if not username or not email or not password:
        return jsonify({"error": "All fields are required!"}), 400
    
    # Check if user already exists
    if any(user['email'] == email for user in users):
        return jsonify({"error": "User already exists!"}), 400

    # Add user to mock database
    user = {"username": username, "email": email, "password": password}
    users.append(user)
    return jsonify({"message": "User signed up successfully!", "user": user}), 201

if __name__ == '__main__':
    app.run(debug=True)
