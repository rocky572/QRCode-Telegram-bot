#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)


import os
from pyrogram import Client,Filters
from telegraph import upload_file
import pyqrcode 
import png 
from messages import msg


@Client.on_message(Filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        
        chat_id=message.chat.id,
        text=f"<b>Hey {message.from_user.first_name},{msg.start}",
        reply_to_message_id=message.message_id,
        parse_mode = "html" 
    )
    
@Client.on_message(Filters.text & Filters.private)
async def qrcode(client, message):
    qr = await client.send_message(
        chat_id=message.chat.id,
        text=f"Creating Your Qr Code..😇",
        reply_to_message_id=message.message_id  
    )
    s = str(message.text)
    qrname = str(message.from_user.id)
    qrcode = pyqrcode.create(s)
    qrcode.png(qrname + '.png', scale = 6) 
    img = qrname + '.png'
    await qr.edit_text("Uploading... ⏫")
    try:
        response = upload_file(img)
    except Exception as error:
        await qr.edit_text(f"{msg.error}")
        return
    try:
        await message.reply_photo(photo=img)

    except Exception as error:
        print(error)

    await qr.edit_text(f"https://telegra.ph{response[0]}")

    try:
        os.remove(img)
    except Exception as error:
        print('Somting is {error}')
         
