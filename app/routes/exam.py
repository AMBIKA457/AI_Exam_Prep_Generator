from fastapi import APIRouter
from app.models.request_model import ExamRequest
from app.services.gemini_service import generate_mcqs

router = APIRouter()

@router.post("/generate")

def generate_mcqs(request: ExamRequest):

    result = (
        request.content
    )

    return {
        "result": result
    }