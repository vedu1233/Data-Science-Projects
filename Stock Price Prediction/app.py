import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Load the scaler (ensure it's saved when you trained the model)
scaler = StandardScaler()

# Set up the Streamlit page
st.set_page_config(page_title="Stock Price Prediction", page_icon="📈", layout="wide")

# Sidebar with navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Contact Us"])

# Apply custom CSS for styling like Google's theme
st.markdown("""
    <style>
        /* General styling for the page */
        body {
            background-color: #f8f9fa;
            font-family: 'Roboto', sans-serif;
        }

        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: #ffffff;
            box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.1);
        }

        /* Styling for the title */
        .stTitle {
            font-size: 30px;
            color: #202124;
            font-weight: 700;
            padding-bottom: 10px;
        }

        /* Styling for subheader */
        .stSubheader {
            font-size: 22px;
            color: #202124;
        }

        /* Styling the prediction button */
        .stButton button {
            background-color: #4285F4;
            color: white;
            font-size: 16px;
            padding: 12px 24px;
            border: none;
            border-radius: 24px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            cursor: pointer;
            transition: background-color 0.3s;
        }

        /* Hover effect for the prediction button */
        .stButton button:hover {
            background-color: #3367D6;
        }

        /* Styling for the input fields */
        .stNumberInput input, .stFileUploader input {
            font-size: 16px;
            border-radius: 6px;
            border: 1px solid #dadce0;
            padding: 10px;
        }

        /* Add some padding to the content */
        .stMarkdown, .stDataFrame, .stWrite {
            padding: 20px;
        }

        /* Box shadows for cards and inputs */
        .stDataFrame, .stFileUploader, .stTextInput {
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            border-radius: 6px;
        }

        /* Styling for contact us section */
        .contact-info {
            font-size: 18px;
            color: #202124;
        }
    </style>
""", unsafe_allow_html=True)

# Home page
if page == "Home":
    st.title("Stock Price Prediction")
    
    # File upload box
    uploaded_file = st.file_uploader("Upload Your Data File (CSV)", type=["csv"])

    if uploaded_file is not None:
        try:
            # Load data into a DataFrame
            data = pd.read_csv(uploaded_file)
            st.write("Data Preview:")
            st.dataframe(data.head())  # Display the first few rows of the uploaded file

            # Check if the required columns exist in the data
            required_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
            if all(col in data.columns for col in required_columns):
                # Prepare the data for prediction (selecting relevant columns)
                input_data = data[required_columns].values
                
                # Scale the input data using the saved scaler
                scaled_data = scaler.fit_transform(input_data)

                # Make predictions for each row and add a new column for the predicted gain
                predictions = model.predict(scaled_data)
                data['Predicted Gain'] = predictions

                # Display the updated dataframe with the predictions
                st.write("Data with Predicted Gains:")
                st.dataframe(data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Predicted Gain']])
                
            else:
                st.error(f"The uploaded file must contain the following columns: {', '.join(required_columns)}")

        except Exception as e:
            st.error(f"Error reading file: {e}")

    # Input fields for user to enter stock data manually (optional for additional prediction)
    st.subheader("Enter Stock Data Manually")

    input1 = st.number_input("Enter Stock Opening Price", min_value=0.0, step=0.01, key="input1")
    input2 = st.number_input("Enter Stock High Price", min_value=0.0, step=0.01, key="input2")
    input3 = st.number_input("Enter Stock Low Price", min_value=0.0, step=0.01, key="input3")
    input4 = st.number_input("Enter Stock Close Price", min_value=0.0, step=0.01, key="input4")
    input5 = st.number_input("Enter Stock Adjusted Close Price", min_value=0.0, step=0.01, key="input5")
    input6 = st.number_input("Enter Stock Volume", min_value=0, step=1, key="input6")

    # Collect all inputs into a list for prediction
    all_inputs = [[input1, input2, input3, input4, input5, input6]]

    # Prediction when the user presses the button
    if st.button("Predict"):
        # Ensure the input is not empty or invalid
        if any(val == 0 for val in all_inputs[0]):
            st.error("Please enter valid values for all inputs.")
        else:
            # Scale the inputs using the saved scaler
            scaled_inputs = scaler.transform(all_inputs)

            # Make the prediction using the model
            pred = model.predict(scaled_inputs)
            st.success(f"The predicted gain is: {pred[0]:.2f}")

# Contact Us page
if page == "Contact Us":
    st.title("Contact Us")

    # Contact information
    st.markdown("""
        <div class="contact-info">
            <strong>Name:</strong> Vedant Pawar<br>
            <strong>Phone Number:</strong> 8459385371<br>
            <strong>Email:</strong> <a href="mailto:vedant@gmail.com">vedant@gmail.com</a><br>
        </div>
    """, unsafe_allow_html=True)

    # Additional contact message
    st.write("Feel free to reach out for any queries related to Stock Price Prediction or this project!")
