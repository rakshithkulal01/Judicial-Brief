import google.generativeai as genai

def ai_extract_clauses(text):
    model = genai.GenerativeModel('gemini-pro')
    prompt = (
        "Extract and list all key clauses (statutes, sections, articles) and all cited precedents from the following legal document. "
        "Format as JSON with keys: clauses, precedents.\n\n"
        f"Document:\n{text}"
    )
    response = model.generate_content(prompt)
    # Attempt to parse Gemini output if structured as JSON
    import json
    try:
        result = json.loads(response.text)
        clauses = result.get("clauses", [])
        precedents = result.get("precedents", [])
    except:
        clauses, precedents = [], []
    return clauses, precedents
