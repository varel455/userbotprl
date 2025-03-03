import asyncio 
import io
import os

import cv2
import requests
from pyrogram import raw

from PyroUbot import *

__MODULE__ = "ɴᴇɢᴀᴛɪᴠᴇ"
__HELP__ = """
<blockquote><b>📚<u>Bantuan Untuk Negative</u>

🚦Perintah : <code>{0}negative</code>
🦠Penjelasan : Untuk Memberikan Efek Negative Ke Gambar</b></blockquote>
"""

@PY.UBOT("negative")
async def negative_cmd(client, message):
    ureply = message.reply_to_message
    ayiin = await message.reply("ᴍᴇᴍᴘʀᴏsᴇs...")
    if not ureply:
        return await ayiin.edit("ʙᴀʟᴀs ᴋᴇ ɢᴀᴍʙᴀʀ")
    ayiinxd = await client.download_media(ureply, "./downloads/")
    if ayiinxd.endswith(".tgs"):
        cmd = ["lottie_convert.py", ayiinxd, "yin.png"]
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
        img = cv2.VideoCapture(ayiinxd)
        heh, lol = img.read()
        cv2.imwrite("yin.png", lol)
        file = "yin.png"
    yinsex = cv2.imread(file)
    kntlxd = cv2.bitwise_not(yinsex)
    cv2.imwrite("yin.jpg", kntlxd)
    await client.send_photo(
        message.chat.id,
        "yin.jpg",
        reply_to_message_id=message.id,
    )
    await ayiin.delete()
    os.remove("yin.png")
    os.remove("yin.jpg")
    os.remove(ayiinxd)