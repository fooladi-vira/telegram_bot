from http import client
from pyrogram import Client
from api import api_hash,api_id,token
from plugins import hello,translate

# app=Client('bot_telegram',api_id,api_hash,bot_token=token)

# with app:
#     for i in range(10) :
#         app.send_message('@engineer210867','hiii')

# app.start()

plugins = dict(root="plugins")
app=Client('bot_telegram',api_id,api_hash,bot_token=token,plugins=plugins)
app.run()
app.send_message('@engineer210867','hiii')

