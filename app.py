import streamlit as st
import pandas as pd
import plotly.express as px

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

# Add a plotly express box plot of price by vehicle type
st.write("### Price Distribution by Vehicle Type")
fig = px.box(df, x="type", y="price", title="Price Distribution by Vehicle Type")
st.plotly_chart(fig)