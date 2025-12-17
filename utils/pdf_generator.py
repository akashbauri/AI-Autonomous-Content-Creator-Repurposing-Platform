from fpdf import FPDF
import os

FONT_PATH = "assets/fonts/DejaVuSans.ttf"

def generate_pdf(content: dict, language="English") -> bytes:
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.add_font("DejaVu", "", FONT_PATH, uni=True)
    pdf.set_font("DejaVu", size=12)

    for section, text in content.items():
        pdf.set_font("DejaVu", size=14)
        pdf.multi_cell(0, 10, section)
        pdf.ln(3)

        pdf.set_font("DejaVu", size=11)
        for para in text.split("\n"):
            pdf.multi_cell(0, 8, para)
            pdf.ln(1)

        pdf.add_page()

    # ✅ Correct way (NO encode)
    return pdf.output(dest="S")
