from fastapi import FastAPI
from groq import Groq
from .models import MedicalRequest
from .utils import clean_text
import os
app = FastAPI(title="MedQuery API")

# Insert your API key here
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Best available model from your list
MODEL_NAME = "llama-3.3-70b-versatile"


@app.post("/qa")
async def medical_qa(req: MedicalRequest):
    """
    Q&A based on the medical report.
    """
    report = clean_text(req.report)
    question = req.question or "Explain this report in simple terms."

    prompt = f"""
    You are a medical assistant AI.
    Use ONLY the medical report below to answer the question clearly,
    safely, and in simple language.

    --- Medical Report ---
    {report}

    --- Question ---
    {question}
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    return {"answer": response.choices[0].message.content}


@app.post("/summarize")
async def summarize(req: MedicalRequest):
    """
    Summarizes the medical report in 3 formats.
    """
    report = clean_text(req.report)

    prompt = f"""
    Summarize the following medical report in EXACTLY 3 formats:

    1. Short summary (2–3 lines)
    2. Detailed clinical summary
    3. Doctor-style structured summary

    --- Medical Report ---
    {report}
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    return {"summary": response.choices[0].message.content}
