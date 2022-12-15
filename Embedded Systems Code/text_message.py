from twilio.rest import Client

account_sid = "ACd178e541067c698f6980aea9e6e5539c"
auth_token = "9a8e4c5573bd87ec1cf3c50250ece5cd"

client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
                to="+16462151374",
                from_="+12075219831",
                body = "Hi Prathamesh!")

