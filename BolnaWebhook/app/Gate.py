from fastapi import FastAPI
from app.routes import bolnaWebhook
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Bolna to Slack Webhook Service")

app.include_router(bolnaWebhook.router)