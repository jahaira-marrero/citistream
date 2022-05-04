
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdx
#import plotly.express as px
import requests

url= "https://data.cityofnewyork.us/resource/h9gi-nx95.json"
data = pd.read_json(url, convert_dates=['crash_date', 'crash_time'])
st.dataframe(data)
#data['crash_date'] = pd.to_datetime(data['crash_date'], infer_datetime_format=True)

st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a streamlit dashboard that can be used to analyze motorvehicle collisions in NYC.")
st.write(data)
#st.write(data.head())





           


  
