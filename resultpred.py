import streamlit as st
import joblib

model=joblib.load("my_marksmodel.pkl")
st.title("Student Pass/Fail Predictor")
st.write("Enter Your Marks")

marks = st.number_input("Enter Your Marks:",min_value=0,max_value=100)

if st.button("Predict"):
 result=model.predict([[marks]])
 if result[0]==1:
  st.success("You are Pass")
 else:
  st.error("Sorry You are Fail")