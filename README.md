# Solar-Farm-Data-Analysis

# Solar Farm Data Analysis Dashboard

## Overview
This project aims to analyze solar farm data from three different countries (Benin, Sierra Leone, and Togo) and visualize key insights using a Streamlit dashboard. The dashboard provides various exploratory data analysis (EDA) tools and visualizations to help MoonLight Energy Solutions make data-driven decisions regarding strategic solar investments.

## Features
- Summary statistics: Calculate mean, median, standard deviation, and other statistical measures for each numeric column.
- Data quality check: Identify missing values, outliers, or incorrect entries.
- Time series analysis: Analyze how solar radiation components and temperature measures change over time.
- Correlation analysis: Determine relationships between different variables.
- Wind analysis: Explore wind speed and wind direction data.
- Temperature analysis: Compare module temperatures with ambient temperature.
- Histograms: Visualize frequency distribution of key variables.
- Box plots: Examine spread and presence of outliers in the data.
- Scatter plots: Explore relationships between pairs of variables.

## Data
The solar farm data is extracted and aggregated from environmental measurements, containing the following columns:
- Timestamp
- GHI (Global Horizontal Irradiance)
- DNI (Direct Normal Irradiance)
- DHI (Diffuse Horizontal Irradiance)
- ModA (Measurement from Module A)
- ModB (Measurement from Module B)
- Tamb (Ambient Temperature)
- RH (Relative Humidity)
- WS (Wind Speed)
- WSgust (Maximum Wind Gust Speed)
- WSstdev (Standard Deviation of Wind Speed)
- WD (Wind Direction)
- WDstdev (Standard Deviation of Wind Direction)
- BP (Barometric Pressure)
- Cleaning (Signifies cleaning event)
- Precipitation (Precipitation rate)
- TModA (Temperature of Module A)
- TModB (Temperature of Module B)
- Comments (Additional notes)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/solar-farm-analysis.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Navigate to the project directory:
   ```bash
   cd solar-farm-analysis
   ```
2. Run the Streamlit dashboard:
   ```bash
   streamlit run dashboard.py
   ```
3. Access the dashboard in your web browser using the provided URL.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or additional features.

Feel free to customize and expand upon this template as needed for your project.
