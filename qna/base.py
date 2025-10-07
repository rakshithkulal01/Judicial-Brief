class QnaInput:
    def __init__(self, document_text, question, chat_history=None):
        self.document_text = document_text
        self.question = question
        self.chat_history = chat_history or []

class QnaOutput:
    def __init__(self, answer, confidence=None):
        self.answer = answer
        self.confidence = confidence or "medium"
