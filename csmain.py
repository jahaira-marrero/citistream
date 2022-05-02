
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdx
#import plotly.express as px
# from sodapy import Socrata
import requests

DATA_URL= requests.get("https://data.cityofnewyork.us/resource/h9gi-nx95.json")

st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a streamlit dashboard that can be used to analyze motorvehicle collisions in NYC.")

def load_data():
    data = pd.json_normalize(DATA_URL.json())
    #data = pd.json_normalize(DATA_URL.json(), nrows =nrows, parse_dates=[['CRASH_DATE', 'CRASH_TIME']])
    return st.dataframe(data)

data = load_data




           


  
