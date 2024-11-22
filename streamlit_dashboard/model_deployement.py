import streamlit as st
import pickle
with open("pickel_file_name",'rb') as file:
    model = pickle.load(file)

st.title('Machine learning with model with deployement')

# making the input field for thr user

input_feature_1 =st.number_input("enter a number")
input_feature_2 =st.number_input("entr the second number 2")

# prediction button 
if st.button("predict"):
    input_data =[[input_feature_1,input_feature_2]]
    prediction = model.predict(input_data)
    st.write(f"prediction {prediction[0]}")

