import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

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

# 1. Histogram of vehicle prices (inside checkbox)
if st.checkbox("Show Histogram of Vehicle Prices"):
    fig1 = px.histogram(df, x='price', nbins=50, 
                        title='Distribution of Vehicle Prices',
                        labels={'price': 'Price ($)', 'count': 'Number of Vehicles'})
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1)

# 2. Histogram of vehicle age (always shown)
st.write("### Distribution of Vehicle Model Years")
fig2 = px.histogram(df, x='model_year', nbins=30,
                    title='Distribution of Vehicle Model Years',
                    labels={'model_year': 'Model Year', 'count': 'Number of Vehicles'})
fig2.update_layout(showlegend=False)
st.plotly_chart(fig2)

# 3. Scatterplot: Price vs Odometer reading (always shown)
st.write("### Vehicle Price vs Odometer Reading")
fig3 = px.scatter(df, x='odometer', y='price', 
                  title='Vehicle Price vs Odometer Reading',
                  labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'},
                  opacity=0.6)
st.plotly_chart(fig3)

# 4. Scatterplot: Price vs Model Year, colored by condition (always shown)
st.write("### Vehicle Price vs Model Year by Condition")
fig4 = px.scatter(df, x='model_year', y='price', color='condition',
                  title='Vehicle Price vs Model Year by Condition',
                  labels={'model_year': 'Model Year', 'price': 'Price ($)'})
st.plotly_chart(fig4)
