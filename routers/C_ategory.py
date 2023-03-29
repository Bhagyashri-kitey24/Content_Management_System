from fastapi import FastAPI, status, HTTPException,APIRouter
from database import db 
import models
from typing import List
from schema import *

router=APIRouter()

# API for Category

# display all Category
@router.get('/category',response_model=List[C_response],status_code=200)
def get_all_category():
   categories=db.query(models.Category).all()
   return categories

#get specific Category
@router.get('/category/{category_id}',response_model=Category)
def get_an_category(category_id:int):
    category=db.query(models.Category).filter(models.Category.category_id==category_id).first()
    return category

@router.get('/csearch/{category_id}',response_model=C_response)
def get_an_category(category_id:int):
    category=db.query(models.Category).filter(models.Category.category_id==category_id).first()
    return category

#ceate Category to database
@router.post('/category',response_model=C_response,status_code=status.HTTP_201_CREATED)
def create_an_post(category:Category):
            new_category=models.Category(    
            # category_id= category.category_id,
            category_name= category.category_name,
            )         
            db.add(new_category)
            db.commit()
            return new_category


#for update Category or edit an Category......post here
@router.put('/category/{category_id}',response_model=Category,status_code=status.HTTP_200_OK)
def update_an_category(category_id:int,category:Category):
    category_to_update=db.query(models.Category).filter(models.Category.category_id==category_id).first()#fetching the desire record.
    #now we need to modify
    # category_to_update.category_id=category.category_i
    category_to_update.category_name=category.category_name
    
    db.commit() #Commiting changes

    return category_to_update

#for deleting Category
@router.delete('/category/{category_id}')
def delete_category(category_id:int):
    category_to_delete=db.query(models.Category).filter(models.Category.category_id==category_id).first()
    if category_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="category Not Found")
    
    db.delete(category_to_delete)
    db.commit()

    return category_to_delete