from pyrogram import filters
from pyrogram.types.bots_and_keyboards import callback_query
import re
from ..config import app
# import utils here
# from ..utils.task_handler import newTask, remove_task, msg_formatter
# import plugins here
# from ..plugins.status import status_window

@app.on_message(filters.command("start"))
async def start(_, message):
    text = 'Alive!'
    await app.send_message(message.chat.id, text)