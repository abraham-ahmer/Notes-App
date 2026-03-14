from fastapi import APIRouter, Depends, HTTPException
from models import UserResponse, UserCreate
from sqlalchemy.orm import Session
from database import get_db
from database_models import User
from utils import hash_pass


router = APIRouter(tags=["Signup"])

@router.post("/signup", response_model=UserResponse)
def sign_up(credentials:UserCreate, db:Session = Depends(get_db)):

    #initially hash the psswrd
    hash = hash_pass(credentials.password)
    credentials.password = hash 

    #check karo k user pehly se hi exist tw nahi karta
    db_user = db.query(User).filter(User.email == credentials.email).first()
    
    if db_user: #if user with same email exist, raise error
        raise HTTPException(status_code=409, detail="User already there")
    
    #if not, then add new user
    new = User(**credentials.dict())
    
    db.add(new)
    db.commit()
    db.refresh(new)
    return new















