from pyrogram import idle 
from app_name.config import app, version, session

app.start()
print(f"Initialised {session} v{version}")
idle()
app.stop()
