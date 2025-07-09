import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(page_title="Used Cars Explorer", page_icon="🚗", layout="wide")

# Set a title and description
st.title("🚗 Used Cars Dataset Explorer")
st.markdown("""
Welcome! 👋  
This interactive dashboard lets you explore used car listings in the U.S.  
Even if you're not a data expert, this app will help you visualize trends in pricing, model years, mileage, and more.
""")

# Load the data
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")

df = load_data()

# Show a preview of the dataset (first 100 rows)
with st.expander("📄 Click to preview the dataset (first 100 rows)", expanded=False):
    st.dataframe(df.head(100), use_container_width=True)

# Sidebar instructions and checkboxes
st.sidebar.header("📊 Select Visualizations")
st.sidebar.write("Choose the charts you'd like to display:")

show_price_hist = st.sidebar.checkbox("Histogram of Vehicle Prices")
show_year_hist = st.sidebar.checkbox("Histogram of Vehicle Model Years")
show_price_odometer = st.sidebar.checkbox("Scatterplot: Price vs Odometer")
show_price_year_condition = st.sidebar.checkbox("Scatterplot: Price vs Model Year by Condition")

# 1. Histogram of Vehicle Prices
if show_price_hist:
    st.subheader("💰 Distribution of Vehicle Prices")
    st.markdown("This histogram shows how car prices are distributed. Are most cars under $10,000? Take a look!")
    fig1 = px.histogram(df, x='price', nbins=50,
                        title='Distribution of Vehicle Prices',
                        labels={'price': 'Price ($)', 'count': 'Number of Vehicles'})
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)

# 2. Histogram of Vehicle Model Years
if show_year_hist:
    st.subheader("📅 Distribution of Vehicle Model Years")
    st.markdown("See which model years are most common among the listings.")
    fig2 = px.histogram(df, x='model_year', nbins=30,
                        title='Distribution of Vehicle Model Years',
                        labels={'model_year': 'Model Year', 'count': 'Number of Vehicles'})
    fig2.update_layout(showlegend=False)
    st.plotly_chart(fig2, use_container_width=True)

# 3. Scatterplot: Price vs Odometer Reading
if show_price_odometer:
    st.subheader("📈 Vehicle Price vs. Odometer Reading")
    st.markdown("This scatterplot shows how mileage affects price. In general, lower mileage = higher price.")
    fig3 = px.scatter(df, x='odometer', y='price',
                      title='Vehicle Price vs Odometer Reading',
                      labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'},
                      opacity=0.6)
    st.plotly_chart(fig3, use_container_width=True)

# 4. Scatterplot: Price vs Model Year by Condition
if show_price_year_condition:
    st.subheader("🛠️ Vehicle Price vs. Model Year by Condition")
    st.markdown("This plot compares car prices and model years, color-coded by vehicle condition.")
    fig4 = px.scatter(df, x='model_year', y='price', color='condition',
                      title='Vehicle Price vs Model Year by Condition',
                      labels={'model_year': 'Model Year', 'price': 'Price ($)'})
    st.plotly_chart(fig4, use_container_width=True)

# Footer message
st.markdown("---")
st.markdown("Made with ❤️ using [Streamlit](https://streamlit.io). Explore trends in the used car market at your own pace!")