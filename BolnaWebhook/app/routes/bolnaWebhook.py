from fastapi import APIRouter, Request, HTTPException
from app.services.B2STransformMain import transform_bolna_to_slack
from app.services.slackRequest import slack_request
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/bolna-webhook")
async def receive_call_data(request: Request):
    try:
        data = await request.json()

        logger.info(f"Incoming payload: {data}")

        if data['status'] == "completed":

            transformed_payload = transform_bolna_to_slack(data)

            await slack_request(transformed_payload)

            return {"status": "success"}
        else:
            print("Different Request Status")

    except Exception as e:
        logger.exception("Webhook processing failed")
        raise HTTPException(status_code=500, detail=str(e))