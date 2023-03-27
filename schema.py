from pydantic import BaseModel

class User(BaseModel):  #serializer
    name:str
    username: str
    mobile_number: str
    email_id: str
    password: str
    role: str 
    profile_photo: int
    bio: str
    
    class Config:
       orm_mode=True
       
       
class Post(BaseModel):  #serializer
    p_id: int
    p_title: str 
    p_description :str 
    is_featured :bool 
    is_published : bool 
    posted_by : int  
    post_category : int 
    media_id : int  
    p_status : bool  
    
    class Config:
       orm_mode=True
       
class Category(BaseModel):
    category_id:int
    category_name:str
    
    class Config:
       orm_mode=True