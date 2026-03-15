from fastapi import APIRouter, Depends, HTTPException
from models import UserResponse, UserCreate
from sqlalchemy.orm import Session
from database import get_db
from database_models import User
from utils import verify_pass
from oauth2 import create_token_access
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["login"])

@router.post("/login")
def login(credentials: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    
    db_user = db.query(User).filter((User.email == credentials.username) | (User.username == credentials.username)).first()

    # if email didnt match
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email")
    
    #if pswrd didnt match
    if not verify_pass(credentials.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid password")
    
    # if right, give em tokens
    payload = {"user_id": db_user.id}
    access_token = create_token_access(payload)
    return {"access_token":access_token, "token_type":"bearer"}






