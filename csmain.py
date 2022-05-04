
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdx
#import plotly.express as px
import requests

url= "https://data.cityofnewyork.us/resource/h9gi-nx95.json"

st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a streamlit dashboard that can be used to analyze motorvehicle collisions in NYC.")


st.cache(persist=True)
def load_data(nrows):
           data = pd.read_json(url, convert_dates=['crash_date', 'crash_time'], lines=True, chunksize=nrows)
           data.dropna(subset = ['latitude', 'longitude'], inplace=True)
           return data

data = load_data(100000)

st.write(data)





           


  
