from fastapi import FastAPI,status,HTTPException
from routers import U_ser, P_ost,C_ategory, Authentication,C_omment



app=FastAPI()

app.include_router(U_ser.router)
app.include_router(P_ost.router)
app.include_router(C_ategory.router)
app.include_router(C_omment.router)
app.include_router(Authentication.router)












#from pydantic import BaseModel
#from typing import Optional,List
#from database import SessionLocal
#from schema import User, Post , Uresponse, P_response ,Role_update ,Feature_update
#from passlib.context import CryptContext
#from database import db
#import models, schema



#router=APIRouter()
#going to implement routs that are implemented in our database

# db=SessionLocal() #implements routes

# #API for User

# @app.get('/users',response_model=List[Uresponse],status_code=200)
# def get_all_users():
#     users=db.query(models.User).all()
#     return users
        
# @app.get('/user/{user_id}',response_model=Uresponse)
# def get_an_user(user_id:int):
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
#     user=db.query(models.User).filter(models.User.user_id==user_id).first()
#     return user


# xyz= CryptContext(schemes=["bcrypt"], deprecated="auto")            
# @app.post('/user',response_model=Uresponse,status_code=status.HTTP_201_CREATED)
# def create_an_user(user:User):
#         db_user=db.query(models.User).filter(models.User.username==user.username).first()
#         if db_user is not None:
#                 raise HTTPException(status_code=400,details="you have already account")
            
#         password_hashing= xyz.hash(user.password) 
    
#         new_user=models.User(
#                 name=user.name,
#                 username=user.username,
#                 mobile_number=user.mobile_number,
#                 email_id=user.email_id,
#                 password=password_hashing,
#                 #role=user.role,
#                 profile_photo=user.profile_photo,
#                 bio=user.bio      
# ) 
#         db.add(new_user)
#         db.commit()
#         return new_user
        
# @app.put('/user/{username}',response_model=User,status_code=status.HTTP_200_OK)
# def update_an_user(username:str,user:User):
#             user_to_update=db.query(models.User).filter(models.User.username==username).first()
    
#             user_to_update.name=user.name,
#             user_to_update.username=user.username,
#             user_to_update.mobile_number=user.mobile_number
#             user_to_update.email_id=user.email_id
#             user_to_update.password=user.password
#             user_to_update.profile_photo=user.profile_photo
#             user_to_update.bio=user.bio
#             db.commit()
#             return user_to_update

# @app.put('/role/{username}',response_model=Uresponse,status_code=status.HTTP_200_OK)
# def update_an_user(username:str,user:Role_update):
#             user_to_update=db.query(models.User).filter(models.User.username==username).first()
    
#             user_to_update.role=user.role
            
#             db.commit()
#             return user_to_update



# @app.delete('/user/{username}')
# def delete_user(username:str):
#     user_to_delete=db.query(models.User).filter(models.User.username==username).first()

#     if user_to_delete is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
    
#     db.delete(user_to_delete)
#     db.commit()

#     db.refresh(user_to_delete)
    
#     return user_to_delete


#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------



# #API for Post

# @app.get('/posts',response_model=List[schema.Post],status_code=200)
# def get_all_posts():
#     posts=db.query(models.Post).all()
#     return posts
        

# @app.get('/post/{p_id}',response_model=P_response)
# def get_an_post(p_id:int):
#     post=db.query(models.Post).filter(models.Post.p_id==p_id).first()
#     return post
            
        
# @app.post('/post',response_model=P_response,status_code=status.HTTP_201_CREATED)
# def create_an_post(post:Post):
#             db_post=db.query(models.Post).filter(models.Post.p_id==post.p_id).first()
#             if db_post is not None:
#                 raise HTTPException(status_code=400,details="you have already account")
                        
#             new_post=models.Post(    
#             p_id= post.p_id,
#             p_title = post.p_title,
#             p_description = post.p_description ,
#             #is_featured = post.is_featured,
#             is_published = post.is_published ,
#             posted_by = post.posted_by,
#             post_category = post.post_category,
#             media_id = post.media_id 
            
#             )
           
            
#             db.add(new_post)
#             db.commit()
#             return new_post
                
# @app.put('/post/{p_id}',response_model=Post,status_code=status.HTTP_200_OK)
# def update_an_post(p_id:int,post:Post):
#             post_to_update=db.query(models.Post).filter(models.Post.p_id==p_id).first()            
#             post_to_update.p_id = post.p_id
#             post_to_update.p_title = post.p_title
#             post_to_update.p_description = post.p_description 
#             #post_to_update.is_featured = post.is_featured
#             post_to_update.is_published = post.is_published 
#             post_to_update.posted_by = post.posted_by
#             post_to_update.post_category = post.post_category
#             post_to_update.media_id = post.media_id 
#             #post_to_update.p_status = post.p_status
#             db.commit()
#             return post_to_update

# @app.put('/feature/{p_id}',response_model=P_response,status_code=status.HTTP_200_OK) #admin side apdation of feature of post
# def update_an_user(p_id:str,post:Feature_update):
#             post_to_update=db.query(models.Post).filter(models.Post.p_id==p_id).first() 
    
#             post_to_update.is_featured = post.is_featured
            
#             db.commit()
#             return post_to_update


# @app.delete('/post/{p_id}')
# def delete_post(p_id:int):
#     post_to_delete=db.query(models.Post).filter(models.Post.p_id==p_id).first()

#     if post_to_delete is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post Not Found")
    
#     db.delete(post_to_delete)
#     db.commit()

#     db.refresh(post_to_delete)
    
#     return post_to_delete

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

#API for Category

#display all items

# @app.get('/category',response_model=List[Category],status_code=200)
# def get_all_category():
#    categories=db.query(models.Category).all()
#    return categories

# #get specific item

# @app.get('/category/{category_id}',response_model=Category)
# def get_an_category(category_id:int):
#     category=db.query(models.Category).filter(models.Category.category_id==category_id).first()
#     return category

# #add items to database
# @app.post('/category',response_model=Category,status_code=status.HTTP_201_CREATED)
# def create_an_post(category:Category):
#             db_category=db.query(models.Category).filter(models.Category.category_id==category.category_id).first()
#             if db_category is not None:
#                 raise HTTPException(status_code=400,details="you have already account")
            
#             new_category=models.Category(    
#             category_id= category.category_id,
#             category_name= category.category_name,
#             )         
#             db.add(new_category)
#             db.commit()
#             return new_category


# #for update schema or edit an item......post here
# @app.put('/category/{category_id}',response_model=Category,status_code=status.HTTP_200_OK)
# def update_an_category(category_id:int,category:Category):
#     category_to_update=db.query(models.Category).filter(models.Category.category_id==category_id).first()#fetching the desire record.
#     #now we need to modify
#     category_to_update.category_id=category.category_id
#     category_to_update.category_name=category.category_name
    
#     db.commit() #Commiting changes

#     return category_to_update

# #for deleting 
# @app.delete('/category/{category_id}')
# def delete_category(category_id:int):
#     category_to_delete=db.query(models.Category).filter(models.Category.category_id==category_id).first()
#     if category_to_delete is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="category Not Found")
    
#     db.delete(category_to_delete)
#     db.commit()

#     return category_to_delete