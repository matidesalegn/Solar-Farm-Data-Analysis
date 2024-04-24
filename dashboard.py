# Importing necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Change the current working directory to the directory of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Current Working Directory:", os.getcwd())

# Function to read CSV files with existence check
def read_csv_with_check(filename):
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        st.error(f"File '{filename}' not found.")
        return None

# Now you can read the CSV files without specifying the full path
benin_data = read_csv_with_check('./data/benin-malanville.csv')
sierra_leone_data = read_csv_with_check('./data/sierraleone-bumbuna.csv')
togo_data = read_csv_with_check('./data/togo-dapaong_qc.csv')

# Function to perform EDA
def perform_eda(data, country_name):
    if data is None:
        return
    st.header(f"Exploratory Data Analysis for {country_name}")
    
    # Displaying summary statistics
    st.subheader("Summary Statistics")
    st.write(data.describe())
    
    # Data Quality Check
    st.subheader("Data Quality Check")
    st.write("Missing Values:")
    st.write(data.isnull().sum())
    
    # Time Series Analysis
    st.subheader("Time Series Analysis")
    time_series_cols = ["Timestamp", "GHI", "DNI", "DHI", "Tamb"]
    time_series_data = data[time_series_cols].set_index("Timestamp")
    st.line_chart(time_series_data)
    
    # Correlation Analysis
    st.subheader("Correlation Analysis")
    numeric_data = data.select_dtypes(include=['float64', 'int64'])  # Select only numeric columns
    corr = numeric_data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    st.pyplot()
    
    # Wind Analysis
    st.subheader("Wind Analysis")
    wind_cols = ["WS", "WSgust", "WSstdev", "WD", "WDstdev"]
    st.write(data[wind_cols].describe())
    
    # Temperature Analysis
    st.subheader("Temperature Analysis")
    temperature_cols = ["Tamb", "TModA", "TModB"]
    st.write(data[temperature_cols].describe())
    
    # Histograms
    st.subheader("Histograms")
    hist_cols = ["GHI", "DNI", "DHI", "WS", "Tamb"]
    for col in hist_cols:
        plt.figure(figsize=(8, 6))
        sns.histplot(data[col], kde=True)
        plt.title(f"Histogram of {col}")
        st.pyplot()
    
    # Box Plots
    st.subheader("Box Plots")
    box_cols = ["GHI", "DNI", "DHI", "Tamb"]
    for col in box_cols:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=data[col])
        plt.title(f"Box Plot of {col}")
        st.pyplot()
    
    # Scatter Plots
    st.subheader("Scatter Plots")
    scatter_cols = [("GHI", "Tamb"), ("WS", "WSgust")]
    for col1, col2 in scatter_cols:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=data[col1], y=data[col2])
        plt.title(f"Scatter Plot of {col1} vs {col2}")
        st.pyplot()

# Create Streamlit dashboard
st.title("Solar Farm Data Analysis Dashboard")
st.sidebar.title("Select Country")

country = st.sidebar.selectbox(
    "Select a country:",
    ("Benin", "Sierra Leone", "Togo")
)

if country == "Benin":
    perform_eda(benin_data, "Benin")
elif country == "Sierra Leone":
    perform_eda(sierra_leone_data, "Sierra Leone")
else:
    perform_eda(togo_data, "Togo")