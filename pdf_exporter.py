from fpdf import FPDF

def build_summary_pdf(summary, key_points, clauses, precedents, file_path="output.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Legal Document Summary", ln=True)

    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, "Summary:", ln=True)
    pdf.multi_cell(0, 10, summary)
    
    pdf.cell(0, 10, "Key Points:", ln=True)
    for point in key_points:
        pdf.multi_cell(0, 10, f"- {point}")
    
    pdf.cell(0, 10, "Clauses:", ln=True)
    for clause in clauses:
        pdf.multi_cell(0, 10, f"- {clause}")
    
    pdf.cell(0, 10, "Precedents:", ln=True)
    for prec in precedents:
        pdf.multi_cell(0, 10, f"- {prec}")
    
    pdf.output(file_path)
    return file_path
