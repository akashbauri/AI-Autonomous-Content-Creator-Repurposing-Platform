from fpdf import FPDF
import os

def generate_pdf(content_dict):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    font_path = os.path.join("assets", "fonts", "DejaVuSans.ttf")

    # Register Unicode font
    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", size=12)

    for title, text in content_dict.items():
        pdf.set_font("DejaVu", size=14)
        pdf.cell(0, 10, title, ln=True)

        pdf.set_font("DejaVu", size=11)
        pdf.multi_cell(0, 8, text)
        pdf.ln(5)

    # Return bytes (NO latin-1 encoding)
    return pdf.output(dest="S")
