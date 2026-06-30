from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

import os

def create_pdf(report, sources):

    try:

        # Create folder if not exists
        os.makedirs(
            "generated_pdfs",
            exist_ok=True
        )

        # File path
        filepath = os.path.join(
            "generated_pdfs",
            "research_report.pdf"
        )

        # Create PDF
        doc = SimpleDocTemplate(filepath)

        styles = getSampleStyleSheet()

        elements = []

        # Title
        elements.append(
            Paragraph(
                "Autonomous Research Report",
                styles["Title"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        # Report content
        report_text = report.replace(
            "\n",
            "<br/>"
        )

        elements.append(
            Paragraph(
                report_text,
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        # Sources heading
        elements.append(
            Paragraph(
                "Sources",
                styles["Heading2"]
            )
        )

        # Source links
        for s in sources:

            elements.append(
                Paragraph(
                    s["url"],
                    styles["BodyText"]
                )
            )

        # Build PDF
        doc.build(elements)

        print("PDF Created Successfully")

        return filepath

    except Exception as e:

        print("PDF Error:", e)

        return ""