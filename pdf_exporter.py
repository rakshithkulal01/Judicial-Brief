from fpdf import FPDF
from fpdf.enums import XPos, YPos
import datetime

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 15)
        self.cell(0, 10, 'AI-Generated Judicial Summary', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        page_num = f'Page {self.page_no()}/{{nb}}'
        self.cell(0, 10, page_num, border=0, new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')

def create_summary_pdf(data: dict):
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 10, 'Document Analysis Report', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(0, 5, f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
    pdf.ln(10)

    # Summary Section
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 10, '1. Executive Summary', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
    pdf.set_font('Helvetica', '', 11)
    pdf.multi_cell(0, 5, data.get('summary', 'No summary provided.'), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)

    # Key Points Section
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 10, '2. Key Points', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
    pdf.set_font('Helvetica', '', 11)
    key_points = data.get('key_points', [])
    if not key_points:
        pdf.multi_cell(0, 5, "No key points were extracted.", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    else:
        for point in key_points:
            pdf.multi_cell(0, 5, f'- {point}', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)

    # You can add similar sections for clauses, precedents, etc., here if desired

    # Return bytes for FastAPI Response—absolutely no .encode()!
    return bytes(pdf.output(dest='S'))

