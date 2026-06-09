# 🫁 Lung Cancer Detection System

## 📌 Project Overview

Lung Cancer Detection System is an Artificial Intelligence (AI) based project that helps detect lung cancer from histopathology images.

The system uses **Deep Learning** and **Computer Vision** techniques to classify lung tissue images into different categories.

This project is made for **educational and demonstration purposes**.

---

## 🎯 Objective

The main goal of this project is:

- Detect lung cancer using histopathology images
- Help understand how AI works in healthcare
- Generate prediction reports automatically
- Visualize affected areas using Grad-CAM heatmap

---

## 🧠 Technologies Used

This project is developed using:

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| TensorFlow | Deep Learning Model |
| Streamlit | Web Application UI |
| OpenCV | Image Processing |
| Plotly | Data Visualization |
| ReportLab | PDF Report Generation |
| VGG16 | Transfer Learning Model |

---

## 🫁 Lung Cancer Classes

The system can detect:

1. **Normal Lung Tissue**
2. **Lung Adenocarcinoma**
3. **Lung Squamous Cell Carcinoma**

---

## ⚙️ Features

✅ Upload histopathology image

✅ AI-based cancer prediction

✅ Confidence score visualization

✅ Grad-CAM heatmap generation

✅ PDF report generation

✅ Patient name validation

✅ Interactive graphs

✅ Premium Medical Dashboard UI

---

## 📂 Project Structure

```text
Lung_Cancer_Detection_System/
│── app.py
│── train.py
│── gradcam.py
│── report.py
│── requirements.txt
│── README.md
│
├── model/
│   └── best_lung_model.h5
│
├── static/
│   ├── uploads/
│   ├── reports/
│   └── temp/
```

---

## 📸 How It Works

### Step 1: Enter Patient Name
The user enters the patient name.

### Step 2: Upload Image
Upload a lung histopathology image.

### Step 3: AI Prediction
The AI model predicts:

- Normal Lung Tissue
- Lung Adenocarcinoma
- Lung Squamous Cell Carcinoma

### Step 4: Confidence Graph
The system displays confidence scores using graphs.

### Step 5: Grad-CAM Heatmap
The system highlights important regions in the image.

### Step 6: Generate PDF Report
A medical-style PDF report is generated automatically.

---

## 🤖 Deep Learning Model

This project uses **VGG16 Transfer Learning Model**.

### Why VGG16?

VGG16 is a pre-trained deep learning model that helps in:

- Better feature extraction
- Faster training
- Higher accuracy
- Better image classification

---

## 📊 Dataset

The dataset contains lung histopathology images divided into:

```text
dataset/
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

## 🚀 How to Run Project

### Step 1: Install Python

Install:

**Python 3.10.11 (Recommended)**

⚠ Important: TensorFlow may not work properly with Python 3.14 or higher.

---

### Step 2: Install Libraries

Run:

```bash
pip install -r requirements.txt
```

---

### Step 3: Run Project

Run:

```bash
streamlit run app.py
```

---

### Step 4: Open Browser

Open:

```text
http://localhost:8501
```

---

## 📈 Model Training

To train model:

Run:

```bash
python train.py
```

The trained model will be saved as:

```text
best_lung_model.h5
```

---

## ⚠ Disclaimer

This project is developed only for:

- Educational purpose
- Learning purpose
- Demonstration purpose

This system is **NOT a medical diagnosis tool**.

Always consult professional doctors for medical diagnosis.

---

## 👨‍💻 Developer



B.Tech / Engineering Student

AI & Deep Learning Project