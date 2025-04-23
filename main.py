from telegram.ext import ApplicationBuilder, CommandHandler
from handlers.start import start  # path to your start handler
from handlers.help_command import help_command
from handlers.status_handler import status
from handlers.github_handler import trigger_github_workflow
from config import TELEGRAM_TOKEN

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("trigger", trigger_github_workflow))

    app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
