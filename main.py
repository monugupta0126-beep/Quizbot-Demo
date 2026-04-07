from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import register

app = Client(
    "quizbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

register(app)

print("✅ Ultra Advanced Bot Running...")
app.run()
