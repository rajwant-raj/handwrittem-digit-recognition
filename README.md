# ✍️ Handwritten Digit Recognition using CNN and Streamlit

This project is a deep learning-based digit recognition system that identifies handwritten digits (0 to 9) drawn on a virtual canvas.  
It uses a Convolutional Neural Network (CNN) trained on the MNIST dataset and features an interactive web interface built with **Streamlit**.

---

## 🎯 Objective

To create an intuitive, browser-based app where users can draw a digit and receive instant predictions from a trained deep learning model.

---

## 🧠 Technologies Used

- **Python 3**
- **TensorFlow / Keras** – For CNN model
- **MNIST Dataset** – For training
- **Streamlit** – For the interactive web interface
- **Pillow** – Image preprocessing
- **NumPy** – Matrix operations
- **streamlit-drawable-canvas** – To allow real-time drawing on canvas

---

## 📌 Features

- 🧠 Predict digit using trained CNN model
- 📊 Displays confidence score and class probabilities
- 🎯 ~98.6% test accuracy using the MNIST dataset
- ⚡ Fast and responsive with a clean UI

---

## 🧪 Model Overview

- **Dataset**: MNIST (60,000 training + 10,000 testing images)
- **Input Shape**: 28×28 grayscale images
- **Architecture**:
  - Conv2D (32 filters, 3×3) → ReLU → MaxPooling
  - Conv2D (64 filters, 3×3) → ReLU → MaxPooling
  - Flatten → Dense (128) → ReLU → Dropout
  - Dense (10) → Softmax
- **Optimizer**: Adam
- **Loss**: Categorical Crossentropy

---

Made with ❤️ by rajwant-raj ✨ | CNN + MNIST + Streamlit
