from twilio.rest import Client

account_sid = 'AC3a6312cda55684bfd04dce439042c802'
auth_token = '6176890dba2b69900b3d830ae4a40408'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="You have to catch up on a lot of anime!",
                     from_='+19386665154',
                     to='+18328085405'
                 )

print(message.sid)