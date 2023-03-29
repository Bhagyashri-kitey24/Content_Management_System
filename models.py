from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text,ForeignKey
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__='users'
    user_id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False)
    username=Column(String(255),nullable=False,unique=True)
    mobile_number=Column(String(50),nullable=False)
    email_id=Column(String(255),nullable=False)
    password=Column(String(255),nullable=False)
    role=Column(String(255),default="author")
    profile_photo=Column(Integer,nullable=True)
    bio=Column(Text)
    
    posts= relationship('Post', back_populates="user")
    
    
class Post(Base):
    __tablename__ = "posts"
    p_id = Column(Integer, primary_key=True)
    p_title = Column(String(255), nullable=False)
    p_description = Column(Text, nullable=False)
    is_featured = Column(Boolean, default=False)
    is_published = Column(Boolean, default=True)
    media_id = Column(Integer,nullable=False)
    # posted_by = Column(Integer,nullable=False) 
    # post_category = Column(Integer,nullable=False)
    
    posted_by = Column(Integer, ForeignKey("users.user_id")) 
    post_category = Column(Integer,ForeignKey("categories.category_id"))    
    
    user= relationship('User', back_populates="posts") #relationship with user
    categories=relationship('Category', back_populates="posts_c") #relationship with Category
    comments= relationship('Comment', back_populates="post_comment")
    
    
class Category(Base):
    __tablename__ = "categories"
    
    category_id= Column(Integer, primary_key=True, index=True)
    category_name = Column(String(50), nullable=False, unique=True)
    
    posts_c=relationship('Post', back_populates="categories")
    
class Comment(Base):
    __tablename__ = "comments"
    
    comment_id= Column(Integer, primary_key=True, index=True)
    comment_description= Column(Text,nullable=False )
    comment_by = Column(String,nullable=False ) 
    
    post_id= Column(Integer,ForeignKey("posts.p_id") )
    
    post_comment=relationship('Post', back_populates="comments")
    
    
    