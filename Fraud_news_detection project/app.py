import streamlit as st
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the model
with open('news_detection.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the TF-IDF Vectorizer
with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Streamlit app title
st.title("Fake News Detection")

# User input
article_text = st.text_area("Enter the article text:")

if st.button("Predict"):
    if article_text:
        # Convert the input text to a DataFrame
        input_data = pd.DataFrame([article_text], columns=['text'])

        # Transform the input text using the TF-IDF vectorizer
        tfidf_features = vectorizer.transform(input_data['text']).toarray()

        # Make predictions using the loaded model
        prediction = model.predict(tfidf_features)

        # Display the prediction result
        if prediction[0] == 1:
            st.success("This article is classified as REAL.")
        else:
            st.error("This article is classified as FAKE.")
    else:
        st.warning("Please enter some text in the article field.")

st.write("1)hou dem aid even see comey letter jason chaffetz tweet darrel lucu")
st.write("2)flynn hillari clinton big woman campu breitbart daniel j flynn")
st.write("3)truth might get fire consortiumnew com")
st.write("4)maci said receiv takeov approach hudson bay new york time michael j de la merc rachel abram")
st.write("5)nato russia hold parallel exerci balkan alex ansari")



 
 
 
 