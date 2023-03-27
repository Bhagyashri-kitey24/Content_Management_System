from fastapi import FastAPI, status, HTTPException, APIRouter
from typing import List
from database import db 
from schema import *
import models


router=APIRouter(tags=["comment"])

@router.get('/comment',response_model=List[Com_response],status_code=200)
def get_all_comment():
   comments=db.query(models.Comment).all()
   return comments

@router.post('/comment',response_model=Com_response,status_code=status.HTTP_201_CREATED)
def create_an_comment(comment:Comment):
            new_comment=models.Comment(    
            post_id= comment.post_id,
            comment_description= comment.comment_description,
            comment_by = comment.comment_by
            )         
            db.add(new_comment)
            db.commit()
            return new_comment

#for deleting 
@router.delete('/comment/{comment_id}')
def delete_comment(comment_id:int):
    comment_to_delete=db.query(models.Comment).filter(models.Comment.comment_id==comment_id).first()
    if comment_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="comment Not Found")
    
    db.delete(comment_to_delete)
    db.commit()

    return comment_to_delete