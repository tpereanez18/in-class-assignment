import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
@st.cache
def load_data():
    df = pd.read_csv('brooklyn_bridge_pedestrians.csv')
    df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
    df.set_index('hour_beginning', inplace=True)
    return df

df = load_data()

# Streamlit app layout
st.title('Brooklyn Bridge Pedestrian Dashboard')

# Resample data for different views
view = st.selectbox('Select View', ['Hourly', 'Daily', 'Weekly'])
if view == 'Hourly':
    resampled_data = df.resample('H').sum()
elif view == 'Daily':
    resampled_data = df.resample('D').sum()
else:
    resampled_data = df.resample('W').sum()

# Display metrics
st.metric(label='Total Pedestrians', value=resampled_data['pedestrians'].sum())
st.metric(label='Average Pedestrians', value=resampled_data['pedestrians'].mean())

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(resampled_data.index, resampled_data['pedestrians'], label='Pedestrians', color='blue')
plt.title('Pedestrian Counts Over Time')
plt.xlabel('Time')
plt.ylabel('Number of Pedestrians')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
st.pyplot(plt)