from fpdf import FPDF
import os

FONT_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "assets",
    "fonts",
    "DejaVuSans.ttf"
)

class UnicodePDF(FPDF):
    pass


def generate_pdf(content_dict):
    pdf = UnicodePDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Register Unicode font
    pdf.add_font("DejaVu", "", FONT_PATH, uni=True)
    pdf.add_font("DejaVu", "B", FONT_PATH, uni=True)

    pdf.set_font("DejaVu", size=11)

    pdf.multi_cell(
        0,
        8,
        "AI Content Report\n"
        "Developed by Akash Bauri\n"
        "AI Engineer | Multi-Agent Systems | LLM Automation\n\n"
    )

    for section, text in content_dict.items():
        pdf.set_font("DejaVu", "B", 13)
        pdf.cell(0, 8, section, ln=True)
        pdf.ln(2)

        pdf.set_font("DejaVu", size=11)
        pdf.multi_cell(0, 8, text)
        pdf.ln(4)

    return pdf.output(dest="S").encode("utf-8")
