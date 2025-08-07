import os
from pyrogram import Client, filters

# گرفتن اطلاعات از Secrets در Replit
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

# تعریف کلاینت Pyrogram
app = Client("my_account", api_id=API_ID, api_hash=API_HASH)

# نوشتن یک هندلر (Handler) برای پاسخ به پیام
@app.on_message(filters.me & filters.command("ping"))
async def ping(_, message):
    await message.edit("Pong!")

# اجرای کلاینت
app.run()
