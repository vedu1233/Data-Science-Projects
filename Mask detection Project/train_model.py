#pip install tensorflow streamlit opencv-python-headless pillow
import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Load the trained CNN model
model = load_model('mask_detector.h5')

# Define a function to preprocess and make predictions on the uploaded image
def predict_mask(image):
    # Resize the image to match the model input shape
    img_resized = cv2.resize(image, (128, 128))
    img_scaled = img_resized / 255.0  # Scale pixel values to [0, 1]
    img_reshaped = np.reshape(img_scaled, [1, 128, 128, 3])  # Reshape for model input

    # Make prediction
    prediction = model.predict(img_reshaped)
    return "Mask" if prediction[0][0] > 0.5 else "No Mask"

# Streamlit UI setup
st.title("Mask Detection App")
st.write("Upload an image to check if the person is wearing a mask.")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert uploaded file to an image
    image = np.array(Image.open(uploaded_file))
    # Display the image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Make prediction and display result
    label = predict_mask(image)
    if label == "Mask":
        st.success("The person in the image is wearing a mask.")
    else:
        st.warning("The person in the image is not wearing a mask.")
