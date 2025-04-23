from fastapi import FastAPI, Request, HTTPException
from config import TELEGRAM_CHAT_ID, TELEGRAM_TOKEN, PROMETHEUS_SECRET
import httpx

app = FastAPI()

@app.post("/alert")
async def receive_alert(request: Request):
    if request.headers.get("X-Secret") != PROMETHEUS_SECRET:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    payload = await request.json()
    alerts = payload.get("alerts", [])
    
    messages = []
    for alert in alerts:
        status = alert.get("status", "UNKNOWN")
        labels = alert.get("labels", {})
        annotations = alert.get("annotations", {})
        msg = f"🚨 [{status}] {labels.get('alertname')} - {annotations.get('summary')}"
        messages.append(msg)

    async with httpx.AsyncClient() as client:
        for message in messages:
            await client.post(
                f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
                json={"chat_id": TELEGRAM_CHAT_ID, "text": message}
            )
    return {"status": "ok"}
