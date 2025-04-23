# handlers/start.py
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = (
        f"👋 Hello {user.first_name or 'there'}!\n\n"
        "I'm CloudMate – your DevOps sidekick. 🚀\n\n"
        "I can help you:\n"
        "✅ Monitor cloud services\n"
        "⚙️ Trigger CI/CD pipelines\n"
        "🚨 Route Prometheus alerts to Telegram\n\n"
        "Choose an option below or use a command to get started:"
    )

    keyboard = [
        ["/status", "/trigger"],
        ["/help"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)
