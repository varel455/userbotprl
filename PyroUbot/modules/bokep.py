from PyroUbot import *

__MODULE__ = "ʙᴏᴋᴇᴘ"
__HELP__ = """
<b>📚<u>Bantuan Untuk Bokep</u></b>

<b>🚦Perintah:</b> <code>{0}bokep</code>
  <b>🦠Penjelasan:</b> Untuk Mengirim VideoRandom
"""

@PY.UBOT("bokep")
async def video_bokep(client, message):
    y = await message.reply_text(emoji("proses") + f"**Mencari Video Bokep**...", quote=True)
    try:
        await client.join_chat("https://t.me/alokshamil")
    except:
        pass
    try:
        bokepnya = []
        async for bokep in client.search_messages(
            -1001867672427, filter=MessagesFilter.VIDEO
        ):
            bokepnya.append(bokep)
        video = random.choice(bokepnya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
    if client.me.id == OWNER_ID:
        return
    await client.leave_chat(-1001867672427)
