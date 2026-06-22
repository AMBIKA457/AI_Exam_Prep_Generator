from fastapi import APIRouter, UploadFile, File
from app.services.pdf_service import extract_text
from app.services.gemini_service import generate_mcqs
import os

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):


    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    extracted_text = extract_text(
        file_path
)

    mcqs = generate_mcqs(
        extracted_text
    )

    return {
        "filename": file.filename,
        "characters": len(extracted_text),
        "preview": extracted_text[:1000],
        "mcqs": mcqs
    }