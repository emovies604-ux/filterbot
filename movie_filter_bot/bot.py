from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("movie_filter_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Import handlers AFTER app is defined
from handlers import start, filter

if __name__ == "__main__":
    app.start()
    print("✅ Bot started successfully!")
    idle()
    app.stop()
    print("🛑 Bot stopped.")
