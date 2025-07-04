import streamlit as st
import pandas as pd

# Set a title
st.title("🚗 Used Cars Dataset Explorer")

# Load the data
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")

df = load_data()

# Show the dataframe
st.write("Here’s a preview of the dataset:")
st.dataframe(df)
