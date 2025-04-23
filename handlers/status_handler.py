from telegram import Update
from telegram.ext import ContextTypes
from utils.http import fetch_status
from config import ENDPOINTS
import aiohttp
import asyncio

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[fetch_status(session, url) for url in ENDPOINTS])
    
    message = "\n".join([f"{url}: {'🟢 ' + str(status) if isinstance(status, int) and status < 400 else '🔴 DOWN'}" for url, status in results])
    await update.message.reply_text(f"🌐 Endpoint Health Check:\n{message}")
