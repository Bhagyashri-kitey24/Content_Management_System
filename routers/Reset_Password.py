from fastapi import FastAPI, status, HTTPException, APIRouter
from routers.U_ser import pwd_context
from routers.Token import create_access_token
from jose import jwt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from database import db 
import models
from schema import * 
#...........
from fastapi.responses import HTMLResponse
from datetime import datetime, timedelta
from pydantic import BaseModel
from typing import Optional

router=APIRouter()


@router.post('/Password',status_code=status.HTTP_201_CREATED)
def create_an_user(user:Reset_pass):    
        db_user=db.query(models.User).filter(models.User.email_id==user.email_id).first()
      
        if not db_user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"You are not a valid user")
       
        Token_reset = create_access_token(data={"email":db_user.email_id})
        
        # Set up the sender's email address and password
        sender_email = "kiteybhagyashri2001@gmail.com"
        sender_password = "koiofcshnrrnvrmw"  
       
    
        # Set up the recipient's email address
        recipient_email = db_user.email_id

        # Create a message object
        message = MIMEMultipart()

        # Set the email subject
        message["Subject"] = "Mail for reset password"

        # Set the sender's email address
        message["From"] = sender_email

        # Set the recipient's email address
        message["To"] = recipient_email

        # Add a message body
        body = f"Token for password reset {Token_reset}" 
        message.attach(MIMEText(body, "plain"))

        # Create an SMTP object
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)

        # Start the TLS encryption
        smtp_connection.starttls()

        # Login to the email server
        smtp_connection.login(sender_email, sender_password)

        # Send the email
        smtp_connection.sendmail(sender_email, recipient_email, message.as_string())

        # Close the SMTP connection
        smtp_connection.quit()    
        
       

        return 'check mail'

# def update_pass(Token_reset,SECRET_KEY):
#     return Token_reset.verify(SECRET_KEY, Token_reset)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
        email = payload.get("email")
        return email
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Token has expired")
    except jwt.exceptions.InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid token")
    
@router.post("/Update_pass/{Token_reset}")
def reset_password(email_id:str, update:Update_pass):

    update_password=db.query(models.User).filter(models.User.email_id==email_id).first()
    
    update_password.password=update.password 
    
  
    db.commit()
    
    # verify token
    email = verify_token()
    if not email:
        raise HTTPException
    
    return 'password reset successfully'
   



    
    
    
    
    
    
    
    
    
    
    
    
    
    
# # verify the token
# def verify_token(token:str):
#     try:
#         payload = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
#         email = payload.get("email_id")
#         return email
#     except jwt.exceptions.ExpiredSignatureError:
#         raise HTTPException(status_code=400, detail="Token has expired")
#     except jwt.exceptions.InvalidSignatureError:
#         raise HTTPException(status_code=400, detail="Invalid token")          
    
             
# @router.get("/reset_password", response_class=Update_pass)
# async def reset_password(token: str):
#     # verify token
#     email = verify_token(token)
#     if not email:
#         raise HTTPException

# def is_valid_token(Token_reset): 
#     if is_valid_token.isalpha():
#         print("Valid token")
#     else:
#         print("Invalid token")