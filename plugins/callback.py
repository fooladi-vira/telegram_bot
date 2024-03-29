from pyrogram import Client,filters
from deep_translator import GoogleTranslator
import asyncio
@Client.on_callback_query()
async def get_callback(client, callback_query):
    await callback_query.answer(
        f"Button contains: '{callback_query.data}'",
    )

