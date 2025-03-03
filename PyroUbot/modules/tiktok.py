import asyncio
import requests
import os
from pyrogram.raw.functions.messages import DeleteHistory
import aiohttp
from PyroUbot import *

__MODULE__ = "ᴛɪᴋᴛᴏᴋ"
__HELP__ = """
<blockquote> <b>Bantuan Untuk Tiktok</b>

• <b>Perintah</b> : <code>{0}tt</code> tt <b>[link nya]</b>
• <b>Penjelasan : Download Vt No wm</b></blockquote>

"""

@PY.UBOT("tt")
async def sosmed_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply(
            f"<code>{message.text}</code> link tiktok"
        )
    else:
        bot = "downloader_tiktok_bot"
        link = message.text.split()[1]
        await client.unblock_user(bot)
        Tm = await message.reply("<code>processing . . .</code>")
        xnxx = await client.send_message(bot, link)
        await asyncio.sleep(10)
        try:
            sosmed = await client.get_messages(bot, xnxx.id + 2)
            await sosmed.copy(message.chat.id, reply_to_message_id=message.id)
            await Tm.delete()
        except Exception:
            await Tm.edit(
                "<b>video tidak ditemukan silahkan ulangi beberapA saat lagi</b>"
            )
        user_info = await client.resolve_peer(bot)
        return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))

