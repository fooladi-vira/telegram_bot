from http import client
from pyrogram import Client
import asyncio
@Client.on_message(group=1)
async def hello(client,message):
    await message.reply('hello'+str(message.from_user.id ))
    
@Client.on_message(group=2)
async def myname(client,message):
    await message.reply(message.from_user.username)