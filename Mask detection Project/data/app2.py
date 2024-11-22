import streamlit as st
import cv2
import numpy as np
from PIL import Image
import pickle
import os

# Specify the full path to the model file (if not in the same directory)
model_path = 'model.pkl'  # Update this if the model is in a different directory

# Check if the model file exists
if not os.path.exists(model_path):
    st.error(f"Model file '{model_path}' not found. Please ensure the model is in the correct directory.")
else:
    # Load the CNN model from pickle file
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    # Set title of the app
    st.title("Mask Detection App")

    # Get the image path from the user
    image_path = st.text_input("Enter the full path to the image:")

    # Check if the path is provided
    if image_path:
        # Load and display the image
        try:
            # Load the image using OpenCV
            input_image = cv2.imread(image_path)

            # Check if the image was loaded successfully
            if input_image is None:
                st.error("Error: Could not load the image. Please check the path and try again.")
            else:
                # Convert the color from BGR to RGB for displaying in Streamlit
                input_image_rgb = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
                st.image(input_image_rgb, caption="Input Image", use_column_width=True)

                # Preprocess the image for model prediction
                input_image_resized = cv2.resize(input_image, (128, 128))
                input_image_scaled = input_image_resized / 255.0
                input_image_reshaped = np.reshape(input_image_scaled, [1, 128, 128, 3])

                # Make prediction
                input_prediction = model.predict(input_image_reshaped)
                input_pred_label = np.argmax(input_prediction)  # Get the predicted label

                # Display prediction result
                if input_pred_label == 1:
                    st.success("The person in the image is wearing a mask.")
                else:
                    st.warning("The person in the image is not wearing a mask.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
