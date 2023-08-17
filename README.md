# Pyrogram Bot

This is a Pyrogram bot that allows certain users to manage chats and users.

## Deploy on Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](http://dashboard.heroku.com/new?template=https://github.com/PRADHAN474/banallpyro)

## Support Group

[![Join our support group](https://img.shields.io/badge/Join%20Group-Support%20Chat-blue.svg)](https://t.me/BWANDARLOK)

## About

This bot is designed to perform certain tasks in designated chats. It's only meant to be used by authorized users.

### Features

- Use `/start` to check if the bot is alive.
- Use `/fuck [chat_id]` to perform certain actions in the chat.
- Use `/unban [chat_id] [user_id]` to unban a user from the chat.

## Configuration

Before using the bot, you need to set up your configuration. Create a `config.py` file with the following content:

```python
SESSION = "your-session-string"
SUDO_USERS = [your_user_ids]
CHATS = [chat_ids]
