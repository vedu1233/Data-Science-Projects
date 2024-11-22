import streamlit as st
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the model
with open('ridge.pickle', "rb") as file:
    model = pickle.load(file)

st.title("Sales Prediction")

# Initialize LabelEncoder for categorical features
le = LabelEncoder()

# Get user inputs
user_input_1 = st.text_input("Item Identifier:")
user_input_2 = st.number_input("Item Weight:")
user_input_3 = st.text_input("Item Fat Content:")
user_input_4 = st.number_input("Item Visibility:")
user_input_5 = st.text_input("Item Type:")
user_input_6 = st.number_input("Item MRP:")
user_input_7 = st.text_input("Outlet Identifier:")
user_input_8 = st.number_input("Outlet Establishment Year:")
user_input_9 = st.text_input("Outlet Size:")
user_input_10 = st.text_input("Outlet Location Type:")
user_input_11 = st.text_input("Outlet Type:")

# Encode categorical inputs
user_input_1 = le.fit_transform([user_input_1])[0]
user_input_3 = le.fit_transform([user_input_3])[0]
user_input_5 = le.fit_transform([user_input_5])[0]
user_input_7 = le.fit_transform([user_input_7])[0]
user_input_9 = le.fit_transform([user_input_9])[0]
user_input_10 = le.fit_transform([user_input_10])[0]
user_input_11 = le.fit_transform([user_input_11])[0]

# Create a list of input values
user_input = [user_input_1, user_input_2, user_input_3, user_input_4, user_input_5, user_input_6,
              user_input_7, user_input_8, user_input_9, user_input_10, user_input_11]

# Make prediction
if st.button("Predict"):
    y_pred = model.predict([user_input])  # Ensure input is a 2D array
    st.write("Total Sales is:", y_pred[0])
