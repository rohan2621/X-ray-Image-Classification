# 🩻 X-Ray Image Classifier (Pneumonia Detection)

A **Streamlit web application** that uses a **TensorFlow/Keras deep learning model** to classify **chest X-ray images** as either:

- **Normal**
- **Pneumonia**

This project is designed to provide **fast and simple pneumonia detection** from chest X-ray images using an uploaded image and a trained deep learning model.

---

## 🚀 Features

- **Real-time Image Upload**
  - Upload chest X-ray images in **JPEG** or **PNG** format.

- **Automated Image Preprocessing**
  - Automatically converts uploaded images to **RGB**
  - Resizes them to **128x128 pixels**

- **Instant Prediction**
  - Predicts whether the X-ray is **Normal** or **Pneumonia**

- **Confidence Score**
  - Displays the prediction along with a **confidence percentage**

- **Simple Web Interface**
  - Easy-to-use UI built with **Streamlit**

---

## 🛠️ Tech Stack

This project is built using the following technologies:

- **Python**
- **Streamlit** – for the web interface
- **TensorFlow / Keras** – for deep learning model loading and inference
- **Pillow (PIL)** – for image processing
- **NumPy** – for numerical operations
- **Pandas** – for data handling (if used in project)

---

## 📋 Prerequisites

Before running this project, make sure you have:

- **Python 3.9+** installed
- A **virtual environment** (recommended)

### Create and Activate Virtual Environment

#### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
