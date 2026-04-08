from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(report, sources):
    file_path = "research.pdf"

    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    elements = []

    # Add report
    elements.append(Paragraph(report, styles["Normal"]))

    # Add references
    elements.append(Paragraph("<b>References:</b>", styles["Heading2"]))

    for i, s in enumerate(sources):
        elements.append(Paragraph(f"{i+1}. {s['title']}", styles["Normal"]))
        elements.append(Paragraph(s["url"], styles["Normal"]))

    doc.build(elements)

    return file_path