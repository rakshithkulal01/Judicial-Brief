class SummarizerInput:
    def __init__(self, text, audience, summary_type, length):
        self.text = text
        self.audience = audience
        self.summary_type = summary_type
        self.length = length

class SummarizerOutput:
    def __init__(self, summary, key_points=None, clauses=None, precedents=None):
        self.summary = summary
        self.key_points = key_points or []
        self.clauses = clauses or []
        self.precedents = precedents or []
