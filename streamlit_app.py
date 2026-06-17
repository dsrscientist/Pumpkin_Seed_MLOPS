
import streamlit as st
import requests

st.title("Pumpkin Seed Classifier")

area = st.number_input("Area")
perimeter = st.number_input("Perimeter")

major_axis = st.number_input("Major Axis Length")
minor_axis = st.number_input("Minor Axis Length")

convex_area = st.number_input("Convex Area")
equiv_diameter = st.number_input("Equiv Diameter")

solidity = st.number_input("Solidity")
roundness = st.number_input("Roundness")

compactness = st.number_input("Compactness")
shape_factor = st.number_input("Shape Factor 1")

if st.button("Predict"):

    payload = {

        "Area": area,
        "Perimeter": perimeter,
        "Major_Axis_Length": major_axis,
        "Minor_Axis_Length": minor_axis,
        "Convex_Area": convex_area,
        "Equiv_Diameter": equiv_diameter,
        "Solidity": solidity,
        "Roundness": roundness,
        "Compactness": compactness,
        "Shape_Factor_1": shape_factor

    }

    response = requests.post(
        "https://pumpkin-seed-mlops.onrender.com/predict",
        json=payload
    )

    prediction=response.json()

    st.success(
        prediction["prediction"]
    )