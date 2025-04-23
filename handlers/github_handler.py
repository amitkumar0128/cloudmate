import aiohttp
from telegram import Update
from telegram.ext import ContextTypes
from config import GITHUB_TOKEN

async def trigger_github_workflow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 2:
        await update.message.reply_text("Usage: /trigger <owner/repo> <workflow_id>")
        return
    
    repo, workflow_id = context.args
    url = f"https://api.github.com/repos/{repo}/actions/workflows/{workflow_id}/dispatches"

    payload = {"ref": "main"}
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as resp:
            if resp.status == 204:
                if update.message:
                    await update.message.reply_text("✅ GitHub Actions workflow triggered.")
                elif update.effective_chat:
                    await context.bot.send_message(chat_id=update.effective_chat.id, text="✅ GitHub Actions workflow triggered.")
                else:
                    print("No way to reply — message and chat are None.")

            else:
                error_text = await resp.text()
                await update.message.reply_text(f"❌ Failed to trigger workflow: {error_text}")
