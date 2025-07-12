import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps
import io


model = tf.keras.models.load_model("my_model.keras")


st.set_page_config(page_title="Handwritten Digit Recognition", page_icon="🔢", layout="centered")


st.sidebar.title("🔧 Options")
st.sidebar.markdown("Upload a 28x28 image of a handwritten digit.")
st.sidebar.info("Model: Trained CNN on MNIST dataset\n\nAccuracy: ~98.6%")


st.title("🖊️ Handwritten Digit Recognition")
st.write("Upload or draw a digit image and the model will predict the digit (0–9).")


uploaded_file = st.file_uploader("📤 Upload Image (PNG, JPG)", type=["png", "jpg", "jpeg"])


def preprocess_image(image):
    image = image.convert("L")                    
    image = ImageOps.invert(image)                  
    image = image.resize((28, 28))                 
    img_array = np.array(image).reshape(1, 28, 28, 1).astype("float32") / 255.0
    return img_array, image

def predict_digit(image_data):
    prediction = model.predict(image_data)
    predicted_label = np.argmax(prediction)
    confidence = float(np.max(prediction))
    return predicted_label, confidence, prediction


if uploaded_file is not None:
    with st.spinner("⏳ Processing Image..."):
        img_data, processed_image = preprocess_image(Image.open(uploaded_file))
        pred_label, confidence, all_probs = predict_digit(img_data)

        st.image(processed_image, caption="🖼️ Processed Image", width=150)

        st.markdown(f"### ✅ Prediction: `{pred_label}`")
        st.markdown(f"**Confidence:** `{confidence*100:.2f}%`")

       
        st.markdown("#### 🔢 Prediction Probability")
        st.bar_chart(data=all_probs[0])

else:
    st.warning("📌 Please upload a digit image to begin.")


st.markdown("---")
st.markdown("<center>Made with ❤️ by rajwant-raj ✨ | CNN + MNIST + Streamlit</center>", unsafe_allow_html=True)
