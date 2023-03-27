from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text

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
    
class Post(Base):
    __tablename__ = "posts"
    p_id = Column(Integer, primary_key=True)
    p_title = Column(String(255), nullable=False)
    p_description = Column(Text, nullable=False)
    is_featured = Column(Boolean, default=False)
    is_published = Column(Boolean, default=True)
    posted_by = Column(Integer, nullable=False)
    post_category = Column(Integer, nullable=False)
    media_id = Column(Integer,nullable=False)
    p_status = Column(Boolean, default=True)
    
    
class Category(Base):
    __tablename__ = "categories"
    category_id= Column(Integer, primary_key=True, index=True)
    category_name = Column(String(50), nullable=False, unique=True)
    
  