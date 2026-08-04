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

## 📸 Application Screenshots

### 🏠 Home Page

<img width="1918" height="971" alt="Screenshot 2026-06-09 174145" src="https://github.com/user-attachments/assets/6a80ff07-911f-41d7-a477-9cdcb424f528" />


**Description:** Landing page for uploading histopathology images.

---

### 🧠 Prediction Dashboard

<img width="1918" height="963" alt="Screenshot 2026-06-09 174207" src="https://github.com/user-attachments/assets/acfa3a3c-51c5-4104-8bee-389f53e1dc48" />


**Description:** Displays AI prediction, confidence score, and Grad-CAM heatmap.

---

### 📊 Confidence Analysis

<img width="1917" height="908" alt="Screenshot 2026-06-09 174224" src="https://github.com/user-attachments/assets/dfa24e91-b08b-4434-acb3-ef54092189b9" />


**Description:** Interactive confidence visualization generated using Chart.js.

---

### 📄 PDF Report & Probability Distribution

<img width="1916" height="683" alt="Screenshot 2026-06-09 174418" src="https://github.com/user-attachments/assets/dda01e3b-9814-4885-b709-8955dba30082" />


**Description:** Shows class probabilities and allows downloading the diagnostic report.

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
