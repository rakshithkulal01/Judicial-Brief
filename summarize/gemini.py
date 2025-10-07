import google.generativeai as genai
from summarize.base import SummarizerInput, SummarizerOutput

import json

# Initialize Gemini (you'll set this in config.py)
def init_gemini(api_key):
    genai.configure(api_key=api_key)

def generate_summary(input: SummarizerInput) -> SummarizerOutput:
    model = genai.GenerativeModel('gemini-pro')
    
    # Create a prompt based on user preferences
    prompt = f"""
    You are an AI legal document summarizer. Please summarize the following legal document.
    
    Audience: {input.audience} (student/lawyer/general)
    Summary Type: {input.summary_type} (concise/bullet/partywise)
    Length: {input.length} (short/medium/long)
    
    Document Text:
    {input.text}
    
    Please provide:
    1. A summary appropriate for the audience
    2. Key points (as a list)
    3. Important clauses mentioned
    4. Legal precedents cited
    
    Format your response as more interactive and user readable keys: summary, key_points, clauses, precedents
    """
    
    response = model.generate_content(prompt)
    
    try:
        # Parse JSON response from Gemini
        result = json.loads(response.text)
        return SummarizerOutput(
            summary=result.get('summary', ''),
            key_points=result.get('key_points', []),
            clauses=result.get('clauses', []),
            precedents=result.get('precedents', [])
        )
    except:
        # Fallback if JSON parsing fails
        return SummarizerOutput(
            summary=response.text,
            key_points=[],
            clauses=[],
            precedents=[]
        )
