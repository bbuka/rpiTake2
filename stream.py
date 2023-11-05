import pandas as pd
# app.py
import streamlit as st

# Title
st.title("My Streamlit App")

# Header
st.header("Welcome to Streamlit!")

# Text
st.text("This is a simple example.")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.text("This is the sidebar.")

# Data Input
user_input = st.text_input("Enter your name:", "John Doe")

# Button
if st.button("Submit"):
    st.success(f"Hello, {user_input}!")

# Plotting
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

st.line_chart(zip(x, y))

# Data Table
data = {'Column 1': [1, 2, 3, 4],
        'Column 2': [10, 20, 30, 40]}
df = st.table(data)

# Display DataFrame
st.dataframe(df)



