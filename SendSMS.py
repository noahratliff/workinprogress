from twilio.rest import Client
import time

# Your Account SID from twilio.com/console
account_sid = "AC902a110f1e50c84df33d1fd8e6a212eb"
# Your Auth Token from twilio.com/console
auth_token  = "46266b58571a81507ede4f6a8c5d4ed2"

client = Client(account_sid, auth_token)

x = 0

#while x < 500:
#    message = client.messages.create(
#        to="+18049302024",
#        from_="+18044156893",
#        body="Prepare yourself")
#    x = x+1
#    print(x)
while x < 100:
    call = client.api.account.calls\
          .create(to="+18045516210",  # Any phone number
                  from_="+18044156893", # Must be a valid Twilio number
                  url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
    time.sleep(1)
    x = x + 1
