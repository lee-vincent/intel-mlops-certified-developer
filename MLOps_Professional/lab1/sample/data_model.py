from pydantic import BaseModel

class MaintenancePayload(BaseModel):
    temperature: int
    pressure: int

class SupportBotPayload(BaseModel):
    msg: str