import os, pymongo
from dotenv import load_dotenv
load_dotenv(dotenv_path=f"{os.getcwd()}/config.env")
from pyrogram import Client

version = os.getenv('VERSION')
session = os.getenv('TELEGRAM_SESSION_NAME')
api_id = int(os.getenv('TELEGRAM_API_ID'))
api_hash = os.getenv('TELEGRAM_API_HASH')
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

app = Client(
	session,
	api_id = api_id,
	api_hash = api_hash,
	bot_token=bot_token)