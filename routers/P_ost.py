from fastapi import FastAPI, status, HTTPException, APIRouter
from typing import Optional,List
from schema import *
import models
from database import db


#API for Post
router=APIRouter()

@router.get('/home',response_model=List[P_response],status_code=status.HTTP_202_ACCEPTED)
def post_to_homepage():
           post_to_homepage=db.query(models.Post).filter(models.Post.is_featured==True).all()
           return post_to_homepage


@router.get('/posts',response_model=List[P_response],status_code=200)
def get_all_posts():
    posts=db.query(models.Post).all()
    return posts
        

@router.get('/post/{p_id}',response_model=P_response)
def get_an_post(p_id:int):
    post=db.query(models.Post).filter(models.Post.p_id==p_id).first()
    return post
            
        
@router.post('/post',response_model=P_response,status_code=status.HTTP_201_CREATED)
def create_an_post(post:Post):
            # db_post=db.query(models.Post).filter(models.Post.p_id==post.p_id).first()
            # if db_post is not None:
            #     raise HTTPException(status_code=400,details="you have already account")
                        
            new_post=models.Post(    
            # p_id= post.p_id,
            p_title = post.p_title,
            p_description = post.p_description ,
            #is_featured = post.is_featured,
            is_published = post.is_published ,
            posted_by = post.posted_by,
            post_category = post.post_category,
            media_id = post.media_id 
            
            )
           
            
            db.add(new_post)
            db.commit()
            return new_post
                
@router.put('/post/{p_id}',response_model=Post,status_code=status.HTTP_200_OK)
def update_an_post(p_id:int,post:Post):
            post_to_update=db.query(models.Post).filter(models.Post.p_id==p_id).first()            
            # post_to_update.p_id = post.p_id
            post_to_update.p_title = post.p_title
            post_to_update.p_description = post.p_description 
            #post_to_update.is_featured = post.is_featured
            post_to_update.is_published = post.is_published 
            # post_to_update.posted_by = post.posted_by
            post_to_update.post_category = post.post_category
            post_to_update.media_id = post.media_id 
            #post_to_update.p_status = post.p_status
            db.commit()
            return post_to_update

@router.put('/feature/{p_id}',response_model=P_response,status_code=status.HTTP_200_OK) #admin side apdation of feature of post
def update_an_user(p_id:str,post:Feature_update):
            post_to_update=db.query(models.Post).filter(models.Post.p_id==p_id).first() 
    
            post_to_update.is_featured = post.is_featured
            
            db.commit()
            return post_to_update

@router.delete('/post/{p_id}')
def delete_post(p_id:int):
    post_to_delete=db.query(models.Post).filter(models.Post.p_id==p_id).first()

    if post_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post Not Found")
    
    db.delete(post_to_delete)
    db.commit()

    db.refresh(post_to_delete)
    
    return post_to_delete
