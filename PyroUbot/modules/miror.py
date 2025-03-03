import asyncio 
import io
import os

import cv2
import requests
from pyrogram import raw

from PyroUbot import *

__MODULE__ = "ᴍɪʀᴏʀ"
__HELP__ = """
<blockquote><b>📚<u>Bantuan Untuk Miror</u></b></blockquote>

<blockquote><b>🚦Perintah : <code>{0}miror</code>
🦠Penjelasan : Untuk Memberikan Efek Cermin Ke Gambar</b></blockquote>
"""

@PY.UBOT("miror")
async def miror_cmd(client, message):
    ureply = message.reply_to_message
    kentu = await message.reply("<i>ᴍᴇᴍᴘʀᴏsᴇs</i>")
    if not ureply:
        return await kentu.edit("ʙᴀʟᴀs ᴋᴇ ɢᴀᴍʙᴀʀ")
    xnxx = await client.download_media(ureply, "./downloads/")
    if xnxx.endswith(".tgs"):
        cmd = ["lottie_convert.py", xnxx, "yin.png"]
        file = "yin.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        img = cv2.VideoCapture(xnxx)
        kont, tol = img.read()
        cv2.imwrite("yin.png", tol)
        file = "yin.png"
    yin = cv2.imread(file)
    mmk = cv2.flip(yin, 1)
    ayiinxd = cv2.hconcat([yin, mmk])
    cv2.imwrite("yin.jpg", ayiinxd)
    await client.send_photo(
        message.chat.id,
        "yin.jpg",
        reply_to_message_id=message.id,
    )
    await kentu.delete()
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(xnxx)
