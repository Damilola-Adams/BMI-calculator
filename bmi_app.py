#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

st.title("BMI Calculator")

name = st.text_input("Enter your name")
weight = st.number_input("Enter your weight (pounds)")
height = st.number_input("Enter your height (inches)")

if st.button("Calculate BMI"):
    bmi = (weight * 703) / (height ** 2)
    st.write(f"Your BMI is **{bmi:.2f}**")

    if bmi < 18.5:
        st.warning(f"{name}, you are underweight. Eattttttttttt!")
    elif bmi <= 24.9:
        st.success(f"{name}, you have a normal weight. Still… you should resume jogging.")
    elif bmi <= 29.9:
        st.warning(f"{name}, you are overweight. You should resume jogging.")
    elif bmi <= 34.9:
        st.error(f"{name}, you are obese. Boyyyyyyyy, exercise!")
    elif bmi <= 39.9:
        st.error(f"{name}, you are severely obese. Damn boy!")
    else:
        st.error(f"{name}, you are morbidly obese. I can't help you.")

