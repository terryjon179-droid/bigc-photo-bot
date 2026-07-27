import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8894654114:AAGEAslb41TkID1IiJch54fQhpMXguOY4_U"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! Welcome.\n\nTell me what you want.\nI can edit pictures. Send me a photo!"
    )

async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📷 I received your photo!"
    )

async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, photo))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
