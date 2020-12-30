from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9608c2f43522e86968475e2d150b5ff5"
# Your Auth Token from twilio.com/console
auth_token = "df7d1058abae3f2df8fd35d3f6eac981"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12105950750",
    from_="+17262008885",
    body="Hello from Python!")

print(message.sid)
