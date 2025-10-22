import json
import os
import hashlib
from datetime import datetime

# File to store users (in production, use a real database)
USERS_FILE = "users.json"

def hash_password(password):
    """Simple password hashing"""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    """Load users from file"""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    """Save users to file"""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def create_user(first_name, last_name, username, email, password, dob, institution):
    """Create a new user"""
    users = load_users()
    
    # Check if user already exists
    if email in users:
        return False, "Email already registered"
    
    # Create user
    users[email] = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "email": email,
        "password": hash_password(password),
        "dob": str(dob),
        "institution": institution,
        "created_at": datetime.now().isoformat()
    }
    
    save_users(users)
    return True, "User created successfully"

def authenticate(email, password):
    """Check if credentials are valid"""
    users = load_users()
    
    if email not in users:
        return False, "User not found"
    
    if users[email]["password"] != hash_password(password):
        return False, "Invalid password"
    
    return True, users[email]

def get_user_by_email(email):
    """Get user information"""
    users = load_users()
    return users.get(email, None)