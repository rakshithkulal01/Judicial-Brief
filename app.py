from fastapi import FastAPI, Response, File, UploadFile, Form, Body
from fastapi.responses import FileResponse
from pdf_reader import extract_text_from_pdf
from summarize.gemini import generate_summary
from summarize.base import SummarizerInput
from qna.gemini import answer_question
from qna.base import QnaInput
from pdf_exporter import create_summary_pdf
import shutil
import os
import json
from typing import Optional

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    text = extract_text_from_pdf(file_path)
    return {"filename": file.filename, "extracted_text": text[:1000]}

@app.post("/summarize/")
async def summarize_doc(
    text: str = Form(...),
    audience: str = Form(...),
    summary_type: str = Form(...),
    length: str = Form(...)
):
    input_data = SummarizerInput(text, audience, summary_type, length)
    summary_output = generate_summary(input_data)
    return {
        "summary": summary_output.summary,
        "key_points": summary_output.key_points,
        "clauses": summary_output.clauses,
        "precedents": summary_output.precedents
    }

@app.post("/qna/")
async def ask_question(
    document_text: str = Form(...),
    question: str = Form(...),
    chat_history: Optional[str] = Form(default="[]")
):
    try:
        parsed_history = json.loads(chat_history) if chat_history else []
    except:
        parsed_history = []
    input_data = QnaInput(document_text, question, parsed_history)
    qna_output = answer_question(input_data)
    return {
        "question": question,
        "answer": qna_output.answer,
        "confidence": qna_output.confidence
    }

@app.post("/extract/")
async def extract_items(text: str = Form(...)):
    # Make sure ai_extract_clauses_and_precedents is defined somewhere!
    clauses, precedents = ai_extract_clauses_and_precedents(text)
    return {
        "clauses": clauses,
        "precedents": precedents
    }

from fastapi import Body, Response

@app.post("/export-pdf/")
async def export_pdf(payload: dict = Body(...)):
    pdf_file = create_summary_pdf(payload)
    headers = {
        "Content-Disposition": "attachment; filename=AI_Judicial_Summary.pdf"
    }
    return Response(content=pdf_file, media_type="application/pdf", headers=headers)
