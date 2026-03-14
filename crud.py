from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from database_models import User, Post
from models import UserCreate, UserResponse, PostCreate, PostResponse
from sqlalchemy.orm import Session
from oauth2 import get_current_user
from typing import List

router = APIRouter(prefix="/posts", tags=["CRUD"])

# add a post
@router.post("/", response_model=PostResponse)
def post(content:PostCreate, db:Session = Depends(get_db), user_credential: User = Depends(get_current_user)):
    
    add_content = Post(**content.dict(), user_id=user_credential.id)

    db.add(add_content)
    db.commit()
    db.refresh(add_content)
    return add_content

#edit a post of a user
@router.put("/{user_id}/edit", response_model=PostResponse)
def edit_post(content:PostCreate, post_id:int, db:Session = Depends(get_db), user_credential: User = Depends(get_current_user)): 
    db_post = db.query(Post).filter(Post.user_id == user_credential.id, Post.id == post_id).first() #user_credential carries user id in the form of uc_id
    
    if not db_post:
        raise HTTPException(status_code=404, detail="Content does not exist")
    
    for key,val in content.dict().items():
        setattr(db_post, key, val)

    db.commit()
    db.refresh(db_post)
    return db_post

#delete a post of a user
@router.delete("/delete")
def delete_post(post_id:int, db:Session = Depends(get_db), user_credential: User = Depends(get_current_user)): 
    db_post = db.query(Post).filter(Post.user_id == user_credential.id, Post.id == post_id).first()

    if not db_post:
        raise HTTPException(status_code=404, detail="Content does not exist")
    
    db.delete(db_post)
    db.commit()
    return {"message":"Post deleted"}


#delete a user and its all the posts
@router.delete("/delete/{user_id}")
def delete_user(db:Session = Depends(get_db), user_credential: User = Depends(get_current_user)): 
    db_user = db.query(User).filter(User.id == user_credential.id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User does not exist")
    
    db.delete(db_user)
    db.commit()
    return {"message": "All the post and account of user is deleted!!"}






#get all posts
@router.get("/", response_model=List[PostResponse])
def get_all(db:Session = Depends(get_db)):
    return db.query(Post).all()


#get 1 post of anyone
@router.get("/{user_id}", response_model=PostResponse)
def get_one_post(id:int, db:Session = Depends(get_db)):
    db_user = db.query(Post).filter(Post.id == id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Content does not exist")
    return db_user


# get all posts of a specific user
@router.get("/user/{user_id}", response_model=list[PostResponse])
def get_users_posts(user_id: int, db:Session = Depends(get_db)):
    db_user = db.query(Post).filter(Post.user_id == user_id).all()

    if not db_user:
        raise HTTPException(status_code=404, detail="Content does not exist")
    
    return db_user





















