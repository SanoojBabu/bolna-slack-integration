from pydantic import BaseModel

class CallPayload(BaseModel):
    id: str
    agent_id: str
    conversation_duration: int
    status: str
    summary: str
    telephony_data: dict