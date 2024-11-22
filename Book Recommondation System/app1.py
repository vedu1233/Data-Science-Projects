import pickle
import streamlit as st
import numpy as np

# Load the similarity score and pivot table
with open("similarity_score.pkl", "rb") as file:
    similarity_score = pickle.load(file)

with open("pt.pkl", "rb") as file1:
    pt = pickle.load(file1)

# Streamlit app layout
st.title("Book Recommendation System")
book_name = st.text_input("Enter Book Name:")

# Recommendation function
def recommend(book_name):
    try:
        # Fetch the index of the book from the pivot table
        index = np.where(pt.index == book_name)[0][0]
        
        # Get similar items based on the similarity score
        similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]
        
        # Display recommended book names
        recommendations = [pt.index[i[0]] for i in similar_items]
        return recommendations
    except IndexError:
        return ["Book not found. Please check the name and try again."]

# Button to get recommendations
if st.button("Recommend"):
    if book_name:
        recommendations = recommend(book_name)
        st.write("Books recommended for you:")
        for rec in recommendations:
            st.write(rec)
    else:
        st.write("Please enter a book name to get recommendations.")
