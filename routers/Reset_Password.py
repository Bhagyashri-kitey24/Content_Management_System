from fastapi import FastAPI, status, HTTPException, APIRouter
from routers.U_ser import pwd_context
from routers.Token import create_access_token , SECRET_KEY 
import jwt
from jwt.exceptions import ExpiredSignatureError,InvalidSignatureError
from passlib.context import CryptContext
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from database import db 
import models
from schema import * 


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
        body = f"Token for password reset:-    {Token_reset}" 
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

        return 'check mail....token send successfully'
    
def token_verify(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        email = payload.get("email")
        return email
    except ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Token has expired")
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid token")
 
 

@router.post("/Update_password/{email_id}/{Token_reset}")

def reset_password(email_id: str, Token_reset: str, update: Update_pass):
    try:
        # Retrieve the user from the database
        user = db.query(models.User).filter(models.User.email_id==email_id).first()
        if user is None:
            return "User not found"
        abc= pwd_context.hash(update.password) 

        user.password = abc
        # Save the changes to the database
        db.commit()
        # Verify the reset token
        token_verify(Token_reset)
        return "Password reset successfully"
    except Exception as e:
        return f"Error resetting password:{str(e)}"   
        print(e) 
    

    
    
    
    
    
