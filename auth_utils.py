import jwt
import datetime

SECRET_KEY= "Signal-forest!22-copper-meteor-pillow-Atlas"

def create_token(username):
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
              }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token


if __name__ == "__main__":
    my_token = create_token("Enthusiast_Dev")
    print(f"My first JWT: {my_token}")