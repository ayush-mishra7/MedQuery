from pydantic import BaseModel

class MedicalRequest(BaseModel):
    report: str
    question: str | None = None
