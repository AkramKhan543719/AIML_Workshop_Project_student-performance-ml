import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("student_model.pkl","rb"))

st.title("Student Math Score Prediction")

reading_score = st.slider("Reading Score",0,100)
writing_score = st.slider("Writing Score",0,100)

if st.button("Predict"):

    features = np.array([[reading_score, writing_score]])

    prediction = model.predict(features)

    st.success(f"Predicted Math Score: {prediction[0]:.2f}")