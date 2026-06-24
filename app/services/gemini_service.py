import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
"gemini-1.5-flash"
)

def generate_mcqs(text):


    prompt = f"""
    Generate 10 multiple choice questions from the content.

    Content:
    {text[:5000]}

Format:

Q1. Question

A) Option A
B) Option B
C) Option C
D) Option D

Answer: A
"""

    response = model.generate_content(
        prompt
    )

    return response.text