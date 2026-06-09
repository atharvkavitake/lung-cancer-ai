# 🫁 AI Lung Cancer Detection System

## 🚀 Overview

The **AI Lung Cancer Detection System** is a Deep Learning-based web application that analyzes histopathology lung tissue images and predicts the presence of lung cancer.

The system leverages **Transfer Learning (VGG16)**, **Computer Vision**, and **Explainable AI (Grad-CAM)** to assist in the classification of lung tissue images into different diagnostic categories.

The application provides:

* AI-powered prediction
* Confidence score visualization
* Grad-CAM explainability
* PDF report generation
* Modern Flask-based web dashboard

---

## 🎯 Project Objectives

* Detect lung cancer from histopathology images
* Demonstrate AI applications in healthcare
* Visualize model attention using Grad-CAM
* Generate downloadable diagnostic reports
* Provide an interactive web-based interface

---

## 🧠 Deep Learning Model

### Transfer Learning: VGG16

This project uses a pre-trained **VGG16 Convolutional Neural Network (CNN)** for feature extraction and classification.

### Advantages

* High-quality feature extraction
* Faster training
* Better generalization
* Improved classification performance

---

## 🫁 Classification Categories

The model classifies images into:

| Class                        | Description         |
| ---------------------------- | ------------------- |
| Normal Lung Tissue           | Healthy Lung Tissue |
| Lung Adenocarcinoma          | Lung Cancer Type    |
| Lung Squamous Cell Carcinoma | Lung Cancer Type    |

---

## ✨ Features

* 📤 Histopathology Image Upload
* 🧠 AI-Based Cancer Prediction
* 📊 Confidence Score Visualization
* 🔥 Grad-CAM Heatmap Generation
* 📄 PDF Report Generation
* 👤 Patient Information Validation
* 🌐 Flask Web Application
* 📱 Responsive Dashboard UI

---

## 🛠 Technology Stack

### Backend

* Python
* Flask
* TensorFlow
* OpenCV
* NumPy

### Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

### Reporting

* ReportLab

### Explainable AI

* Grad-CAM

---

## 📂 Project Structure

```text
LUNG_CANCER_DETECTION_SYSTEM
│
├── app.py
├── gradcam.py
├── report.py
├── requirements.txt
├── Procfile
│
├── model/
│   └── best_lung_model.h5
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── assets/
│   ├── css/
│   ├── js/
│   ├── uploads/
│   ├── reports/
│   └── temp/
│
└── README.md
```

---

## ⚙️ Workflow

### Step 1

User enters patient information.

### Step 2

Histopathology image is uploaded.

### Step 3

The image is preprocessed and passed to the trained VGG16 model.

### Step 4

The model predicts the most probable class.

### Step 5

Confidence scores are visualized using interactive charts.

### Step 6

Grad-CAM highlights important image regions.

### Step 7

A PDF diagnostic report is generated.

---

## 📊 Dataset Structure

```text
dataset/
│
├── train/
│   ├── lung_n
│   ├── lung_aca
│   └── lung_scc
│
└── test/
    ├── lung_n
    ├── lung_aca
    └── lung_scc
```

---

## 💻 Installation

### Clone Repository

```bash
git clone https://github.com/atharvkavitake/lung-cancer-ai.git
```

### Enter Project Folder

```bash
cd lung-cancer-ai
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## 🌐 Local Access

Open:

```text
http://127.0.0.1:5000
```

---

## 🚀 Deployment

This application can be deployed using:

* Render
* Railway
* PythonAnywhere

### Render Start Command

```bash
gunicorn app:app
```

---

## 📸 System Outputs

### Original Histopathology Image

* Uploaded image visualization

### AI Prediction

* Predicted class
* Confidence score

### Grad-CAM Heatmap

* Explainable AI visualization

### PDF Report

* Downloadable medical-style report

---

## ⚠ Disclaimer

This project is intended for:

* Educational purposes
* Research purposes
* Demonstration purposes

This system is **not a certified medical diagnostic tool** and should not be used as a substitute for professional medical advice or diagnosis.

---

## 👨‍💻 Developer

**Atharv Kavitake**

Third Year B.Tech Engineering Student(Artificial Intelligence And Data Science)
Government College Of Engineering, Kolhapur

Artificial Intelligence • Machine Learning • Deep Learning

---

⭐ If you found this project useful, consider giving it a star on GitHub.
