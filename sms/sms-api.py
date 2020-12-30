# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC9608c2f43522e86968475e2d150b5ff5']
auth_token = os.environ['df7d1058abae3f2df8fd35d3f6eac981']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+17262008885',
                     to='+12105950750'
                 )

print(message.sid)
