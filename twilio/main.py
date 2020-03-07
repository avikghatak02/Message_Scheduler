
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client     # it helps to contact with server
import sys 
# sys module is a set of functions which provide crucial information about
# how your Python script is interacting with the host system.
account_sid = 'AC84bf8436aa383b7a45cd7b2a20ac789c'              # Twilio account SID
auth_token = 'password'        # Twilio account auth token
client = Client(account_sid, auth_token)   # we are passing the authentication to the Client class of twilio.rest

message = sys.argv[1]              # taking first argument as message from the terminal
try:
     message_create = client.messages.create(
                body=message,       # your message variable content goes here
                from_='+...', # Your Twilio Phone Number
                to='91....'   # Phone Number on which you want to send message
          )

     print(message_create.sid)     # to print message id in the terminal
except:
     print("Invalid Number")       # any sort of error in sending the message will lead to this exception block