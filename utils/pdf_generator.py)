from fpdf import FPDF

def generate_pdf(content_dict):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "AI Content Report", ln=True)

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 8, "Developed by Akash Bauri\n\n", ln=True)

    for section, text in content_dict.items():
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 8, section, ln=True)
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 7, text)
        pdf.ln(3)

    return pdf.output(dest="S").encode("latin-1")
