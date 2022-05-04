
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdx
#import plotly.express as px
import requests

url= "https://data.cityofnewyork.us/resource/h9gi-nx95.json"
data = pd.read_json(url, convert_dates=['crash_date', 'crash_time'])
data.dropna(subset = ['latitude', 'longitude'], inplace=True)
lowercase = lambda x: str(x).lower()
data.rename(lowercase, axis = 'columns', inplace=True)
date.rename(columns={'crash_date_crash_time': 'date/time'}, inplace=True)



st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a streamlit dashboard that can be used to analyze motorvehicle collisions in NYC.")
st.write(data)





           


  
