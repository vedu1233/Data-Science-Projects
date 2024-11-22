import streamlit as st
import pandas as pd
import joblib
from PIL import Image
#Loading Our final trained Knn model 
model= open("Knn_Classifier.pkl", "rb")
knn_clf=joblib.load(model)
st.title("Iris flower species Classification App")
#Loading images
setosa= Image.open('setosa.png')
versicolor= Image.open('versicolor.png')
virginica = Image.open('virginica.png')
