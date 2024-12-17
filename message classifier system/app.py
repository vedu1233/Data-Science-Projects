import pandas as pd
import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer


def load_model_and_vectorizer():
    try:
        with open("vectorizer1.pkl", "rb") as vec_file:
            vectorizer = pickle.load(vec_file)

        with open("last_model.pkl", "rb") as model_file:
            model = pickle.load(model_file)
    except FileNotFoundError:
        st.error("Required files (last_vectorizer.pkl or last_model.pkl) are missing.")
        st.stop()

    if not hasattr(vectorizer, "vocabulary_"):
        st.error("The vectorizer is not properly fitted. Check your training process.")
        st.stop()

    return model, vectorizer

model, vectorizer = load_model_and_vectorizer()

# Define label mapping
label_mapping = {
    0: "Spam",                
    1: "Fraud",                
    2: "OTP",                  
    3: "Promotions/Offers",   
    4: "Transaction",          
    5: "Banking/Account Updates",
    6: "Logistics",            
}

# Suggested actions for each category
suggested_actions = {
    "Spam": "Delete the message or unsubscribe if applicable. Report it as spam.",
    "Fraud": "Do not respond. Report the fraud to your bank or service provider.",
    "OTP": "Verify the OTP immediately. Do not share it with anyone.",
    "Promotions/Offers": "Check out the offers and decide if they are relevant to you.",
    "Transaction": "Check your bank account for accuracy and flag any fraudulent transactions.",
    "Banking/Account Updates": "Review your banking or account details for any updates or changes.",
    "Logistics": "Track your shipment using the provided details or website."
}

# App title
st.title("Message Classifier App")

# Input message
message = st.text_input("Enter a message to classify")

# Classifying the message and suggesting actions
if st.button("Classify Message"):
    if message.strip():
        try:
            # Transform the input message and predict
            predicted_label = model.predict(vectorizer.transform([message]))[0]
            category = label_mapping.get(predicted_label, "unknown")
            st.write(f"**Message Category:** {category}")

            # Suggest actions based on message category
            action = suggested_actions.get(category, "No suggested action available.")
            st.write(f"**Suggested Action:** {action}")
        except Exception as e:
            st.error(f"Error during classification: {e}")
    else:
        st.warning("Please enter a valid message.")
