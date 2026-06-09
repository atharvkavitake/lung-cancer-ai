from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Paragraph,
    Image,
    Table,
    TableStyle,
    PageBreak
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_CENTER


def generate_pdf(
    patient_name,
    uploaded_image_path,
    predicted_class,
    probability_dict,
    gradcam_path,
    output_path,
    timestamp
):

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    heading_style = styles["Heading2"]
    body_style = styles["BodyText"]

    title_style.alignment = TA_CENTER
    title_style.textColor = colors.HexColor(
        "#0EA5E9"
    )

    story = []

    # ---------------- HEADER ----------------
    story.append(
        Paragraph(
            "AI LUNG DIAGNOSIS REPORT",
            title_style
        )
    )

    story.append(Spacer(1, 12))

    story.append(
        Paragraph(
            "<font color='#64748B'>"
            "AI Powered Histopathology "
            "Analysis Dashboard"
            "</font>",
            body_style
        )
    )

    story.append(Spacer(1, 20))

    # ---------------- PATIENT INFO ----------------
    story.append(
        Paragraph(
            "Patient Information",
            heading_style
        )
    )

    patient_table = Table([
        ["Patient Name", patient_name],
        ["Date & Time", timestamp]
    ])

    patient_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#0F172A")
            ),

            (
                "BACKGROUND",
                (0, 0),
                (-1, -1),
                colors.HexColor("#E2E8F0")
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, -1),
                colors.black
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.grey
            ),

            (
                "FONTNAME",
                (0, 0),
                (-1, -1),
                "Helvetica-Bold"
            )
        ])
    )

    story.append(patient_table)

    story.append(Spacer(1, 20))

    # ---------------- PREDICTION ----------------
    story.append(
        Paragraph(
            "Prediction Summary",
            heading_style
        )
    )

    prediction_color = "#16A34A"

    if predicted_class == \
            "Lung Adenocarcinoma":

        prediction_color = "#F59E0B"

    elif predicted_class == \
            "Lung Squamous Cell Carcinoma":

        prediction_color = "#DC2626"

    story.append(
        Paragraph(
            f"""
            <font color='{prediction_color}'>
            <b>Predicted Result:</b>
            {predicted_class}
            </font>
            """,
            body_style
        )
    )

    story.append(Spacer(1, 20))

    # ---------------- CONFIDENCE TABLE ----------------
    story.append(
        Paragraph(
            "Prediction Confidence Scores",
            heading_style
        )
    )

    confidence_data = [
        ["Class", "Confidence (%)"]
    ]

    for label, prob in probability_dict.items():

        confidence_data.append([
            label,
            f"{prob * 100:.2f}%"
        ])

    confidence_table = Table(
        confidence_data
    )

    confidence_table.setStyle(
        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#0EA5E9")
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),

            (
                "BACKGROUND",
                (0, 1),
                (-1, -1),
                colors.HexColor("#F8FAFC")
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.grey
            ),

            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            )
        ])
    )

    story.append(confidence_table)

    story.append(Spacer(1, 20))

    # ---------------- ORIGINAL IMAGE ----------------
    story.append(
        Paragraph(
            "Uploaded Histopathology Image",
            heading_style
        )
    )

    story.append(
        Image(
            uploaded_image_path,
            width=250,
            height=250
        )
    )

    story.append(Spacer(1, 20))

    # ---------------- GRADCAM ----------------
    story.append(
        Paragraph(
            "Grad-CAM Heatmap Analysis",
            heading_style
        )
    )

    story.append(
        Image(
            gradcam_path,
            width=250,
            height=250
        )
    )

    story.append(Spacer(1, 20))

    # ---------------- DISCLAIMER ----------------
    story.append(
        Paragraph(
            "<font color='red'>"
            "<b>Disclaimer:</b>"
            "</font>"
            " This AI system is developed "
            "for educational and demonstration "
            "purposes only. It must not be "
            "used as a substitute for "
            "professional medical diagnosis.",
            body_style
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "<font color='#64748B'>"
            "Generated by Lung Cancer "
            "Detection AI Dashboard"
            "</font>",
            body_style
        )
    )

    doc.build(story)