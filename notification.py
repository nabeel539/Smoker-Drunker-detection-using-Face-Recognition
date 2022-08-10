import os
from twilio.rest import Client
def msg():
	account_sid='AC49d1894dc619da49224ed6dff4bee008'
	auth_token='0dc818c368907e46c04593f506feb0a8'
	client=Client(account_sid,auth_token)
	message=client.messages.create(
                       body="Someone caught while intoxicated...Plz check.  ",
                       from_='+19855319036',
                       to='+919937505876'


                       )
	print(message.sid)
