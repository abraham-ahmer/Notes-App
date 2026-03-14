from jose import JWTError, jwt
from models import UserCreate
from datetime import datetime, timedelta
from models import TokenData
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from database import get_db
from sqlalchemy.orm import Session
from database_models import User

SECRET_KEY = "secret_random_text_for_verification"
ALGORITHM = "HS256"
EXPIRATION_TIME = 30


def create_token_access(data:dict):
    to_encode = data.copy() #khaali 

    expiry = datetime.utcnow() + timedelta(minutes=EXPIRATION_TIME)  #expiry time banaya

    to_encode.update({"exp": expiry}) #us expiry ko dict me daala

    jwt_token = jwt.encode(claims=to_encode, key=SECRET_KEY, algorithm=ALGORITHM) #encode krwa dia
    
    return jwt_token


def verify_token_access(data:str, credential_exception):
    try:
        payload = jwt.decode(data, key=SECRET_KEY, algorithms=ALGORITHM)
        us_id = payload.get("user_id")
        if us_id is None:
            raise credential_exception
        return TokenData(id=us_id)
    
    except JWTError:
        raise credential_exception

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(new_token:str = Depends(oauth2_scheme), db:Session = Depends(get_db)):
    new_credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token expired or user does not exist... Can not perform crud activity",
        headers={"WWW-Authenticate": "bearer"}
    )

    token_data = verify_token_access(new_token, new_credential_exception)
    db_user = db.query(User).filter(User.id == token_data.id).first()

    if not db_user:
        raise new_credential_exception
    return db_user







