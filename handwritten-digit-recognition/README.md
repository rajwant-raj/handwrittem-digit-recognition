# 🧠 Handwritten Digit Recognition using CNN

A deep learning project that identifies handwritten digits (0–9) from images using a Convolutional Neural Network (CNN) trained on the MNIST dataset.  
Built with **TensorFlow**, **Streamlit**  for interactive predictions.

---

## 🚀 Features

- 🧠 Predict the digit using a trained CNN model
- 📊 Displays prediction confidence and probability chart
- ✅ Simple, interactive UI with Streamlit

---

## 📦 Project Overview

- 🔍 Dataset: [MNIST (Keras version)](https://keras.io/api/datasets/mnist/)
- 🧠 Model: CNN with ~98.6% accuracy
- 🌐 Interface: Streamlit
- 📊 Features: Confusion matrix + Heatmap + Bar chart confidence

---

## 📁 Folder Structure
digit-recognition-dl/
├── streamlit_app.py # Streamlit web app code
├── my_model.keras  # Trained CNN model
├── handwritten-digit-recognition.ipynb# Colab notebook (training + evaluation)
├── handwritten-digit-recognition.py #python file of colab notebook
├── interface-ui.png # Screenshot of the app
├──sample image.png  # image for testing the model
├──sample image 1.png # image for testing the model 
├── Handwritten Digit Recognition sample.pdf # sample output of the model
├── Handwritten Digit Recognition sample 1.pdf # sample output of the model
├── requirements.txt # Python dependencies
└── README.md


---


🧠 Model Architecture
 2x Conv2D Layers

2x MaxPooling2D Layers

1x Dense Layer (128 units)

1x Output Layer (Softmax, 10 units)


---

📦 Dependencies

streamlit
tensorflow
numpy
Pillow

Install with:

bash
pip install -r requirements.txt


---


## 🚀 How to Run

### 🔧 Setup

bash
git clone https://github.com/your-username/digit-recognition-dl.git
cd digit-recognition-dl
pip install -r requirements.txt

▶️ Run Streamlit App
bash
streamlit run app/streamlit_app.py


---


📊 Results
✅ Test Accuracy: ~98.6%

📉 Loss Curve & Confusion Matrix:

Includes matplotlib + seaborn heatmap

Helps visualize digit classification errors

---

✨ Credits
Dataset: MNIST (by Yann LeCun)

Model: Built using TensorFlow/Keras

UI: Streamlit 

---
👤 Author

 Developed by Rajwant raj
 
 GitHub: github.com/rajwant-raj
 
 LinkedIn: www.linkedin.com/in/rajwant-raj-350519369

❤️ Made For
A deep learning internship project ( at Scalezix ) to demonstrate CNN-based digit recognition with a clean interactive UI using Streamlit.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.




