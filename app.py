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

# Show a preview of the dataset (first 100 rows)
st.write("Here’s a preview of the dataset (first 100 rows):")
st.dataframe(df.head(100))

# Sidebar instructions and checkboxes
st.sidebar.header("Select Visualizations")
st.sidebar.write("Check the charts you'd like to display:")

show_price_hist = st.sidebar.checkbox("Histogram of Vehicle Prices")
show_year_hist = st.sidebar.checkbox("Histogram of Vehicle Model Years")
show_price_odometer = st.sidebar.checkbox("Scatterplot: Price vs Odometer")
show_price_year_condition = st.sidebar.checkbox("Scatterplot: Price vs Model Year by Condition")

# 1. Histogram of Vehicle Prices
if show_price_hist:
    fig1 = px.histogram(df, x='price', nbins=50,
                        title='Distribution of Vehicle Prices',
                        labels={'price': 'Price ($)', 'count': 'Number of Vehicles'})
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1)

# 2. Histogram of Vehicle Model Years
if show_year_hist:
    fig2 = px.histogram(df, x='model_year', nbins=30,
                        title='Distribution of Vehicle Model Years',
                        labels={'model_year': 'Model Year', 'count': 'Number of Vehicles'})
    fig2.update_layout(showlegend=False)
    st.plotly_chart(fig2)

# 3. Scatterplot: Price vs Odometer Reading
if show_price_odometer:
    fig3 = px.scatter(df, x='odometer', y='price',
                      title='Vehicle Price vs Odometer Reading',
                      labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'},
                      opacity=0.6)
    st.plotly_chart(fig3)

# 4. Scatterplot: Price vs Model Year by Condition
if show_price_year_condition:
    fig4 = px.scatter(df, x='model_year', y='price', color='condition',
                      title='Vehicle Price vs Model Year by Condition',
                      labels={'model_year': 'Model Year', 'price': 'Price ($)'})
    st.plotly_chart(fig4)