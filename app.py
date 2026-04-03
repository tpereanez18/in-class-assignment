import streamlit as st
import pandas as pd

# Load data
@st.cache
def load_data():
    return pd.read_csv('brooklyn_bridge_pedestrians.csv')

data = load_data()

# Title and subtitle
st.title('Brooklyn Bridge Pedestrian Traffic Dashboard')
st.subheader('Explore pedestrian counts over time')

# Radio widget for selecting view
view_option = st.radio('Choose view:', ['Hourly', 'Daily', 'Weekly'])

# Resampling logic based on the view
if view_option == 'Hourly':
    resampled_data = data.resample('H').sum()
elif view_option == 'Daily':
    resampled_data = data.resample('D').sum()
else:
    resampled_data = data.resample('W').sum()

# Line chart of pedestrian counts
st.line_chart(resampled_data['counts'])

# Metrics for total and average counts
total_counts = resampled_data['counts'].sum()
average_counts = resampled_data['counts'].mean()

st.metric('Total Pedestrian Counts', total_counts)
st.metric('Average Pedestrian Counts', average_counts)