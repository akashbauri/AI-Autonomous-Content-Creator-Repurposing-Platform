from fpdf import FPDF

class UnicodePDF(FPDF):
    pass


def generate_pdf(content_dict):
    pdf = UnicodePDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Use a Unicode-safe core font
    pdf.set_font("Helvetica", size=11)

    pdf.multi_cell(
        0,
        8,
        "AI Content Report\n"
        "Developed by Akash Bauri\n"
        "AI Engineer | Multi-Agent Systems | LLM Automation\n\n"
    )

    for section, text in content_dict.items():
        pdf.set_font("Helvetica", "B", 13)
        pdf.cell(0, 8, section, ln=True)
        pdf.ln(2)

        pdf.set_font("Helvetica", size=11)
        pdf.multi_cell(0, 8, text)
        pdf.ln(4)

    # ✅ UTF-8 SAFE OUTPUT (NO latin-1)
    return pdf.output(dest="S").encode("utf-8")
