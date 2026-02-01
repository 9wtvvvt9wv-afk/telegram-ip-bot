from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")

def get_public_ip():
    return requests.get("https://api.ipify.org", timeout=5).text

async def ip_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        ip = get_public_ip()
        await update.message.reply_text(f"🌐 Public IP:\n{ip}")
    except:
        await update.message.reply_text("❌ خطا در دریافت IP")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("ip", ip_command))

print("Bot is running...")
app.run_polling()
