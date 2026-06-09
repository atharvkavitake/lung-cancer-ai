from flask import (
    Flask,
    render_template,
    request,
    send_file
)

import tensorflow as tf
import numpy as np
from PIL import Image
import cv2
import os
import datetime
import re

from gradcam import (
    generate_gradcam,
    overlay_heatmap
)

from report import generate_pdf


app = Flask(__name__)

# ---------------- FOLDERS ----------------

UPLOAD_DIR = "static/uploads"
REPORT_DIR = "static/reports"
TEMP_DIR = "static/temp"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

# ---------------- MODEL ----------------

MODEL_PATH = "model/best_lung_model.h5"

CLASS_NAMES = [
    "Normal Lung Tissue",
    "Lung Adenocarcinoma",
    "Lung Squamous Cell Carcinoma"
]

model = tf.keras.models.load_model(
    MODEL_PATH
)

# ---------------- PREPROCESS ----------------

def preprocess_image(image):

    image = image.resize((128,128))

    image = np.array(image)

    image = image / 255.0

    image = np.expand_dims(
        image,
        axis=0
    )

    return image

# ---------------- HOME ----------------

@app.route("/")
def home():

    return render_template(
        "index.html"
    )

# ---------------- PREDICT ----------------

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    patient_name = request.form.get(
        "patient_name"
    )

    uploaded_file = request.files.get(
        "image"
    )

    if not patient_name:

        return "Patient name required"

    if not uploaded_file:

        return "Image required"

    if not re.match(
        r"^[A-Za-z ]+$",
        patient_name.strip()
    ):

        return "Invalid Patient Name"

    timestamp = datetime.datetime.now()\
        .strftime("%Y%m%d_%H%M%S")

    image_path = os.path.join(
        UPLOAD_DIR,
        f"{timestamp}_{uploaded_file.filename}"
    )

    uploaded_file.save(
        image_path
    )

    image = Image.open(
        image_path
    ).convert("RGB")

    img_array = preprocess_image(
        image
    )

    predictions = model.predict(
        img_array,
        verbose=0
    )[0]

    predicted_index = np.argmax(
        predictions
    )

    predicted_class = CLASS_NAMES[
        predicted_index
    ]

    confidence = float(
        predictions[predicted_index]
        * 100
    )

    probability_dict = {

        CLASS_NAMES[i]:
        round(
            float(predictions[i]) * 100,
            2
        )

        for i in range(
            len(CLASS_NAMES)
        )
    }

    # ---------------- GRADCAM ----------------

    heatmap = generate_gradcam(
        model,
        img_array,
        predicted_index
    )

    overlay = overlay_heatmap(
        image,
        heatmap
    )

    gradcam_filename = (
        f"gradcam_{timestamp}.png"
    )

    gradcam_path = os.path.join(
        TEMP_DIR,
        gradcam_filename
    )

    cv2.imwrite(
        gradcam_path,
        cv2.cvtColor(
            overlay,
            cv2.COLOR_RGB2BGR
        )
    )

    # ---------------- PDF ----------------

    report_filename = (
        f"report_{timestamp}.pdf"
    )

    pdf_path = os.path.join(
        REPORT_DIR,
        report_filename
    )

    current_time = datetime\
        .datetime.now()\
        .strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    # generate_pdf(
    #     patient_name,
    #     image_path,
    #     predicted_class,
    #     probability_dict,
    #     gradcam_path,
    #     pdf_path,
    #     current_time
    # )

    return render_template(
        "result.html",

        patient_name=
        patient_name,

        prediction=
        predicted_class,

        confidence=
        round(confidence,2),

        probabilities=
        probability_dict,

        image_path=
        image_path,

        gradcam_path=
        gradcam_path,

        report_path=
        pdf_path
    )

# ---------------- DOWNLOAD REPORT ----------------

@app.route("/download")
def download():

    path = request.args.get(
        "file"
    )

    return send_file(
        path,
        as_attachment=True
    )

# ---------------- MAIN ----------------

if __name__ == "__main__":

    app.run(
        debug=True
    )

