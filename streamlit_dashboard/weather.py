import streamlit as st 
st.title("Weather prediction")

input_1 =st.number_input("Enter Today Tempreture:")
if st.button("submit"):
    if input_1 >=25:
        st.write(f"today tempreture is hot ")
    else:
        

        st.write(f"Today Tempreture is cool")
    

