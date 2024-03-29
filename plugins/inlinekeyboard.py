from pyrogram import Client,filters
from pyrogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

import asyncio
@Client.on_message(filters.text,group=5)
async def keyboard_reply(client,message):
    keyboard_mark=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton('translate to English'),KeyboardButton('ترجمه به فارسی')],
            [KeyboardButton('4'),KeyboardButton('6')]
            ]
    )
    
    await message.reply("k",
    reply_markup=keyboard_mark)


@Client.on_message(filters.text,group=6)
async def keyboard_inline(client,message):
    keyboard_inline=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('',callback_data='s'),InlineKeyboardButton('2',callback_data='translate to English')],
            [InlineKeyboardButton('q',callback_data='qq'),InlineKeyboardButton('w',callback_data='234')]
            ]
    )
    
    await message.reply('s',
    reply_markup=keyboard_inline)