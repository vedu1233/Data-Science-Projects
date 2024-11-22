import streamlit as st 
import seaborn as sns 
st.header("my name is vedant")
st.write("Hello guys my name is vedant")
# create one input field that takes your name 
name = st.text_input("Enter you name")
age = st.number_input("enter your age",min_value=1,max_value =100,step =1)
dob = st.date_input("select your birthdate")
subject = st.text_input("Enter your subject name")
age1 = st.selectbox("choose an option:",['abobe 18','below 18','teenager'])

if st.button("submit"):
    st.write(f"name: {name}")
    st.write(f"age: {age}")
    st.write(f"dob: {dob}")
    st.write(f"subject: {subject}")
    st.write(f"age :{age1}")

