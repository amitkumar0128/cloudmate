# ☁️ CloudMate Bot

CloudMate is a modular Telegram bot that empowers DevOps engineers to monitor cloud services, trigger CI/CD pipelines, and receive infrastructure alerts directly in Telegram. Built with Python and powered by `python-telegram-bot`, it integrates with AWS, GitHub, and Prometheus.

## 🚀 Features

- `/start` – Greets the user and explains bot capabilities.
- `/status` – Check the health of endpoints.
- `/trigger <owner/repo> <workflow_id>` – Trigger GitHub Actions workflow.
- Prometheus Webhook Receiver – Forwards alerts to Telegram.

## ⚙️ Tech Stack

- Python 3.10+
- python-telegram-bot
- aiohttp
- python-dotenv
- GitHub REST API
- Prometheus AlertManager

## 🛠 Setup Instructions

### 1. Clone & Navigate

```bash
git clone https://github.com/yourusername/cloudmate.git
cd cloudmate
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a .env file
```env
TELEGRAM_TOKEN=your-telegram-bot-token
TELEGRAM_CHAT_ID=your-chat-id
GITHUB_TOKEN=your-github-token
PROMETHEUS_SECRET=your-secret
```

## 📟 Prometheus Alert Setup
Send alerts to:

```nginx
POST http://<your-server>:5001/alerts?secret=your-secret
```

Use this in your Prometheus Alertmanager config:

```yaml
receivers:
  - name: 'telegram'
    webhook_configs:
      - url: 'http://your-server:5001/alerts?secret=your-secret'
```

🧪 Example Commands
```bash
/status https://google.com https://example.com
/trigger youruser/yourrepo your_workflow.yml
```

## 🧑‍💻 Author
### Amitkumar
Made with Python.
