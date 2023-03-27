from sqlalchemy.orm import declarative_base     #upon this we will creat module classes
from sqlalchemy import create_engine            #engine which link our sqlalchemy to our database
from sqlalchemy.orm import sessionmaker

#set up sql to work with our sqlalchemy
engine=create_engine("postgresql://postgres:root@localhost/Content_Management_db",echo=True) #echo attribute enable us to see whatever sql is generated

Base=declarative_base() 


SessionLocal=sessionmaker(bind=engine) #help us to run database session wvery time we shall carry out the operations

db=SessionLocal()