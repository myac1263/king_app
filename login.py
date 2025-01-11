import bcrypt
import json

USER_DATA_FILE = "users.json"

# Load existing user data from the file (if it exists)
def load_users():
    try:
        with open(USER_DATA_FILE, "r") as file:
            data = file.read().strip()  # Read and strip any unnecessary whitespace
            if data:  # If file is not empty
                return json.loads(data)  # Parse the JSON content
            else:
                return {}  # Return an empty dictionary if the file is empty
    except (FileNotFoundError, json.JSONDecodeError):  # Handle both file not found or invalid JSON
        return {}  # Return an empty dictionary if the file doesn't exist or contains invalid JSON

# Save the updated user data to the file
def save_users(users):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file)

# Hash the password before saving
def hash_password(password):
    salt = bcrypt.gensalt()  # Automatically generates a salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password  # Return the raw hash (bytes)

# Function to create a new user
def create_user(username, password, role="User"):
    users = load_users()
    if username in users:
        return False  # Username already exists
    
    hashed_password = hash_password(password)  # Get the hashed password
    users[username] = {"password": hashed_password.decode('utf-8'), "role": role}  # Store as string
    save_users(users)
    return True

# Login function to verify user credentials
def login(username, password):
    users = load_users()
    if username in users:
        stored_hash = users[username]["password"].encode('utf-8')  # Get the stored hash as bytes
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            return True
    return False
