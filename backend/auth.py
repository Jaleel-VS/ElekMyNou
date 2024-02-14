from firebase_admin import auth
from fastapi import Depends, HTTPException, status
import cryptic
import hashlib

async def get_current_user(token: str = Depends(auth.verify_id_token)):
    user = auth.get_user(token)

    if user:
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    

def hash_password(password: str):
    salt = cryptic.SALT

    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000);

    return hashed_password.hex()

def verify_password(plain_password: str, hashed_password: str):
    
    return hashed_password == hash_password(plain_password)

if __name__ == "__main__":
    # test the hash_password function

    password = "password"

    hashed_password = hash_password(password)

    print(hashed_password)

    # test the verify_password function

    print(verify_password(password, hashed_password)) # should return True