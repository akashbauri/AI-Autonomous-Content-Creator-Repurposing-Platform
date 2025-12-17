from fpdf import FPDF
import os

FONT_PATH = os.path.join("assets", "fonts", "DejaVuSans.ttf")


class ProfessionalPDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", size=9)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


def generate_pdf(content: dict, reference_link: str, language: str) -> bytes:
    pdf = ProfessionalPDF()
    pdf.set_auto_page_break(auto=True, margin=30)

    pdf.add_font("DejaVu", "", FONT_PATH, uni=True)

    # ---------------- COVER PAGE ----------------
    pdf.add_page()
    pdf.set_font("DejaVu", size=22)
    pdf.multi_cell(0, 14, "AI Professional Content Report", align="C")
    pdf.ln(10)

    pdf.set_font("DejaVu", size=13)
    pdf.multi_cell(
        0,
        10,
        f"Language: {language}\n"
        "Generated using AI-powered content automation.\n\n"
        "Developed by Akash Bauri",
        align="C"
    )

    # ---------------- CONTENT ----------------
    for section, text in content.items():
        pdf.add_page()

        pdf.set_font("DejaVu", size=18)
        pdf.multi_cell(0, 14, section)
        pdf.ln(5)

        pdf.set_draw_color(200, 200, 200)
        pdf.line(30, pdf.get_y(), 180, pdf.get_y())
        pdf.ln(10)

        pdf.set_font("DejaVu", size=12)
        pdf.multi_cell(0, 10, text)
        pdf.ln(12)

        # Clickable reference link
        if reference_link.startswith("http"):
            pdf.set_text_color(0, 0, 255)
            pdf.set_font("DejaVu", size=11)
            pdf.cell(0, 10, f"Reference: {reference_link}", link=reference_link)
            pdf.set_text_color(0, 0, 0)

    return pdf.output(dest="S")
