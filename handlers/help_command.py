from telegram import Update
from telegram.ext import ContextTypes
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "📖 *Available Commands:*\n"
        "/status - Check health of cloud endpoints\n"
        "/trigger - Trigger GitHub Actions workflow\n"
        "/help - Show this message\n"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")
