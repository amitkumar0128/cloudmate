import aiohttp

async def fetch_status(session, url):
    try:
        async with session.get(url, timeout=5) as response:
            return url, response.status
    except Exception:
        return url, "DOWN"
