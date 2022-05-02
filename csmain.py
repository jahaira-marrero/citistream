
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdx
#import plotly.express as px
# from sodapy import Socrata
import requests

#DATA_URL= requests.get("https://data.cityofnewyork.us/resource/h9gi-nx95.json")
url_path = "https://data.cityofnewyork.us/resource/h9gi-nx95.json"
data = pd.read_json(url_path, convert_dates=['CRASH_DATES', 'CRASH_TIME'], nrows=100000, )
#d = pd.to_datetime(data['CRASH_DATE', 'CRASH_TIME'])

st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a streamlit dashboard that can be used to analyze motorvehicle collisions in NYC.")
st.write(data)




           


  
