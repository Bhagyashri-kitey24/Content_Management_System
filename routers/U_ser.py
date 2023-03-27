from fastapi import FastAPI, status,HTTPException , APIRouter
import  models  
from schema import *
# from schema import User , Uresponse, Role_update
from database import SessionLocal
from database import db
from typing import Optional,List 
from passlib.context import CryptContext

#from .. database import SessionLocal
#db=SessionLocal()


router=APIRouter()


#API for User


@router.get('/users',response_model=List[Show_all_Users],status_code=200)
def get_all_users():
    users=db.query(models.User).all()
    return users

                
@router.get('/user/{user_id}',response_model=Uresponse)
def get_an_user(user_id:int):
    user=db.query(models.User).filter(models.User.user_id==user_id).first()
    return user

@router.get('/usearch/{user_id}',response_model=List[Usearch],status_code=200)
def get_all_users():
    users=db.query(models.User).all()
    return users
# @router.get('/usearch/{user_id}',response_model=P_response)
# def get_an_user(user_id:int):
#     user=db.query(models.User).filter(models.User.user_id==user_id).first()
#     return user


pwd_context= CryptContext(schemes=["bcrypt"], deprecated="auto")            
@router.post('/user',response_model=Uresponse,status_code=status.HTTP_201_CREATED)
def create_an_user(user:User):
        db_user=db.query(models.User).filter(models.User.username==user.username).first()
        if db_user is not None:
                raise HTTPException(status_code=400,details="you have already account")
            
        password_hashing= pwd_context.hash(user.password) 
    
        new_user=models.User(
                name=user.name,
                username=user.username,
                mobile_number=user.mobile_number,
                email_id=user.email_id,
                password=password_hashing,
                #role=user.role,
                profile_photo=user.profile_photo,
                bio=user.bio      
) 
        db.add(new_user)
        db.commit()
        return new_user
        
@router.put('/user/{username}',response_model=User,status_code=status.HTTP_200_OK)
def update_an_user(username:str,user:User):
            user_to_update=db.query(models.User).filter(models.User.username==username).first()
    
            user_to_update.name=user.name,
            user_to_update.username=user.username,
            user_to_update.mobile_number=user.mobile_number
            user_to_update.email_id=user.email_id
            user_to_update.password=user.password
            user_to_update.profile_photo=user.profile_photo
            user_to_update.bio=user.bio
            db.commit()
            return user_to_update

@router.put('/role/{username}',response_model=Uresponse,status_code=status.HTTP_200_OK)
def update_an_user(username:str,user:Role_update):
            user_to_update=db.query(models.User).filter(models.User.username==username).first()
    
            user_to_update.role=user.role
            
            db.commit()
            return user_to_update


@router.delete('/user/{username}')
def delete_user(username:str):
    user_to_delete=db.query(models.User).filter(models.User.username==username).first()

    if user_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
    
    db.delete(user_to_delete)
    db.commit()

    db.refresh(user_to_delete)
    
    return user_to_delete
