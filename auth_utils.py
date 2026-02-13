import jwt
import datetime
import os
import hashlib
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY= os.getenv("MY_SUPER_SECRET_KEY")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

USER_DB = {
    "Enthusiast_Dev": "SecurePass123",
    "Admin_User": "PythonIsCool"
}

def authenticate(username, passsword):
    if username in USER_DB and USER_DB[username] == passsword:
        return True
    return False



def create_token(username):
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
              }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token


if __name__ == "__main__":
    user = input("Enter username: ")
    pw = input("Enter password: ")

    if authenticate(user, pw):  
        token = create_token(user)
        print(f"✅ Login Successful! Your Secure Token: {token}")
    else:
        print("❌ Access Denied: Incorrect credentials  .")  
    
