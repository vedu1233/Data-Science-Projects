import streamlit as st 
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
with open('ridge.pkl',"rb") as file:
    model = pickle.load(file)
st.title("Sales Prediction")
import streamlit as st
from sklearn.preprocessing import LabelEncoder
import pickle

le = LabelEncoder()

with open('ridge.pkl', "rb") as file:
    model = pickle.load(file)

st.title("Sales Prediction")

# ... (rest of your input fields)

def predict():
    

    user_input_2 =st.number_input("Item_Weight:")

    

    user_input_4 =st.number_input("Item_Visibility")


    user_input_6 =st.number_input("Item_MRP:")

    

    user_input_8 =st.number_input("Outlet_Establishment_Year:")

    

    

    # Preprocess user input
    user_input_1_encoded = le.transform([user_input_1])[0]
    user_input_3_encoded = le.transform([user_input_3])[0]
    user_input_5_encoded = le.transform([user_input_5])[0]
    user_input_7_encoded = le.transform([user_input_7])[0]
    user_input_9_encoded = le.transform([user_input_9])[0]
    user_input_10_encoded = le.transform([user_input_10])[0]
    user_input_11_encoded = le.transform([user_input_11])[0]

    # Create a list of input values
    user_input = [user_input_1_encoded, user_input_2, user_input_3_encoded, user_input_4, user_input_5_encoded, user_input_6, user_input_7_encoded, user_input_8, user_input_9_encoded, user_input_10_encoded, user_input_11_encoded]

    # Make prediction
    prediction = model.predict([user_input])
    st.write("Predicted Sales:", prediction[0])

if st.button("Predict"):
    predict()