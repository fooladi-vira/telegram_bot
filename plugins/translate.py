from http import client
from pyrogram import Client,filters
from deep_translator import GoogleTranslator
import asyncio
@Client.on_message(filters.text,group=3)
async def tanslate_to_fa(client,message):
    translator=GoogleTranslator('auto','fa')
    translatorE=GoogleTranslator('auto','en')
    txt=message.text.split()
    if txt[0]=='translate':
        message.text.replace('translate',' ')
        translated=translator.translate(message.text)
        await message.reply_text("   /n ترجمه متن انگلیسی به فارسی"+ translated)
    elif txt[0]=='ترجمه':
        #txt[0]=''
        translated=translatorE.translate(message.text)
        await message.reply_text(translated)
    else:
        pass


