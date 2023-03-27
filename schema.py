from pydantic import BaseModel
from typing import List ,Text, Optional  

class User(BaseModel):  #serializer
    name:str
    username: str
    mobile_number: str
    email_id: str
    password: str
    #role: str 
    profile_photo: int
    bio: str
    
    class Config:
       orm_mode=True
       
class Show_all_Users(BaseModel):  #serializer
    user_id:int
    name:str
    username: str
    mobile_number: str
    email_id: str
    role: str 
    profile_photo: int
    bio: str
    
    class Config:
       orm_mode=True 
       

            
class Uresponse(BaseModel):  #serializer
    user_id:int
    name:str
    username: str
    mobile_number: str
    email_id: str
    #password: str 
    role: str 
    profile_photo: int
    bio: str
    posts:List
    
    #posts:Show_posts
    
    class Config:
       orm_mode=True 
       

class Show_posts(BaseModel): # for showing uer id and username in post
    user_id:int
    username: str
    
    class Config:
       orm_mode=True
       

class Show_categories(BaseModel): # for showing category id and name in post
    category_id:int
    category_name:str
    class Config:
       orm_mode=True
       
class Show_comments(BaseModel): # for showing category id and name in post
    comment_by : str
    comment_description : str
    class Config:
       orm_mode=True       

class P_response(BaseModel):  #serializer
    p_id: int
    p_title: str 
    p_description :str 
    is_featured :bool 
    is_published : bool 
    posted_by : int 
    post_category : int 
    media_id : int  

    user:Show_posts
    categories:Show_categories
    comments:List[Show_comments]
    # comments:List
    class Config:
       orm_mode=True     

class Usearch(BaseModel):  #serializer
    user_id:int
    name:str
    username: str
    mobile_number: str
    email_id: str
    #password: str 
    role: str 
    profile_photo: int
    bio: str
    posts:List
    #=[Show_categories]
    # categories:Show_categories
    # categories:List
    #posts:Show_posts
    posts:Show_categories
    class Config:
       orm_mode=True 
       

       
class Role_update(BaseModel):  #serializer
    
    role: str 
    
    class Config:
       orm_mode=True        
       
       
class Post(BaseModel):  #serializer
    # p_id: int
    p_title: str 
    p_description :str 
    #is_featured :bool 
    is_published : bool 
    # posted_by : int
    post_category : int 
    media_id : int  
    
    
    class Config:
       orm_mode=True
       
       

# class Show_posts(BaseModel): # for showing uer id and username in post
#     user_id:int
#     username: str
    
#     class Config:
#        orm_mode=True
       

# class Show_categories(BaseModel): # for showing category id and name in post
#     category_id:int
#     category_name:str
#     class Config:
#        orm_mode=True
       

# class P_response(BaseModel):  #serializer
#     p_id: int
#     p_title: str 
#     p_description :str 
#     is_featured :bool 
#     is_published : bool 
#     posted_by : int 
#     post_category : int 
#     media_id : int  

#     user:Show_posts
#     categories:Show_categories
    
#     class Config:
#        orm_mode=True       
       
       
class Feature_update(BaseModel):  #serializer
    
    is_featured :bool 
    
    class Config:
       orm_mode=True     
       
       
class Category(BaseModel):
    # category_id:int
    category_name:str
    
    class Config:
       orm_mode=True       
              
class C_response(BaseModel):
    
    category_id:int
    category_name:str
    posts_c:List
    
    class Config:
       orm_mode=True



class Comment(BaseModel):
    post_id : int
    comment_description : str
    comment_by : str
   
    class Config:
       orm_mode=True

class Com_response(BaseModel):
    comment_id: int
    post_id : int
    comment_description : str
    comment_by : str
   
       
    class Config:
       orm_mode=True


   
#---------------------------------------------------------------Login------------------------------------
class Login(BaseModel):  #serializer
   
    username: str 
    password: str 
    
    class Config:
       orm_mode=True 
#------------------------------------------------------------------------------------------------------------


class Token(BaseModel):
    access_token: str
    token_type: str
    
    class Config:
        orm_mode = True 


class TokenData(BaseModel):
    username: Optional[str]=None       
  
              
