from fpdf import FPDF
from io import BytesIO
import os

def generate_pdf(content_dict):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # 🔤 Font path (relative to repo root)
    font_path = os.path.join("assets", "fonts", "DejaVuSans.ttf")

    # Register Unicode font
    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", size=11)

    for section, text in content_dict.items():
        # Section title
        pdf.set_font("DejaVu", size=14)
        pdf.multi_cell(0, 10, section)
        pdf.ln(2)

        # Section content
        pdf.set_font("DejaVu", size=11)
        pdf.multi_cell(0, 8, text)
        pdf.ln(6)

    # ✅ Streamlit-safe PDF bytes
    pdf_buffer = BytesIO()
    pdf_buffer.write(pdf.output(dest="S"))
    pdf_buffer.seek(0)

    return pdf_buffer
