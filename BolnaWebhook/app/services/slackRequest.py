import logging

import httpx

from app.core.config import settings

logger = logging.getLogger(__name__)


async def slack_request(payload: dict):
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(
                url=settings.SLACK_WEBHOOK_URL,
                json=payload
            )
            print("STATUS:", response.status_code)
            print("RESPONSE:", response.text)
            response.raise_for_status()

            if response.status_code != 200:
                logger.error(f"Slack error: {response.text}")
                raise Exception("Slack webhook failed")

    except Exception as e:
        logger.exception("Error sending to Slack")
        raise e
