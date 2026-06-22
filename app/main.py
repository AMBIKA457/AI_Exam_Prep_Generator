from fastapi import FastAPI
from app.routes.exam import router
from app.routes.pdf import router as pdf_router

app = FastAPI(
    title="AI Exam Prep Generator"
)

@app.get("/")
def home():
    return {
        "message": "AI Exam Prep Generator API Running"
    }

app.include_router(
    router,
    prefix="/exam",
    tags=["Exam"]
)

app.include_router(
    pdf_router,
    prefix="/pdf",
    tags=["PDF"]
)