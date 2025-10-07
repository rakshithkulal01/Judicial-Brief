import google.generativeai as genai
from .base import QnaInput, QnaOutput

def answer_question(input: QnaInput) -> QnaOutput:
    model = genai.GenerativeModel('models/gemini-2.5-pro')
    
    # Build context with chat history
    context = "Document Content:\n" + input.document_text + "\n\n"
    
    if input.chat_history:
        context += "Previous Conversation:\n"
        for qa in input.chat_history:
            context += f"Q: {qa.get('question', '')}\nA: {qa.get('answer', '')}\n"
    
    prompt = f"""
    {context}
    
    Based on the legal document above and any previous conversation or whatever information available on the internet, please answer this question:
    Question: {input.question}
    
    Provide a clear, accurate answer based only on the document content. If the answer isn't in the document, find it through internet and your knowledge from the database, with reference to the document.
    """
    
    response = model.generate_content(prompt)
    
    return QnaOutput(
        answer=response.text,
        confidence="high"
    )
