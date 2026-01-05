from fpdf import FPDF
import os

def generate_pdf_report(link, violation, severity, confidence, policy, stats_table, filename):
    os.makedirs("Evidence", exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "PARS - Privacy Abuse Report", ln=True, align='C')

    pdf.set_font("Arial", '', 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Link: {link}", ln=True)
    pdf.cell(0, 10, f"Violation: {violation}", ln=True)
    pdf.cell(0, 10, f"Severity: {severity}", ln=True)
    pdf.cell(0, 10, f"Confidence: {confidence}%", ln=True)
    pdf.multi_cell(0, 10, f"Policy: {policy}")

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Statistics Table", ln=True)
    pdf.set_font("Arial", '', 12)
    for row in stats_table:
        pdf.cell(0, 8, f"{row[0]:40} {row[1]}", ln=True)

    pdf.output(filename)
    return filename
