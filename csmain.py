
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdx
#import plotly.express as px
# from sodapy import Socrata
import requests

DATA_URL= requests.get("https://data.cityofnewyork.us/resource/h9gi-nx95.json")
data = pd.json_normalize(DATA_URL.json(), convert_dates=True)
#d = pd.to_datetime(data['CRASH_DATE', 'CRASH_TIME'])

st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a streamlit dashboard that can be used to analyze motorvehicle collisions in NYC.")
st.write(data)




           


  
