from pydantic import BaseModel

class ExamRequest(BaseModel):
    content: str