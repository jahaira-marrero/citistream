
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdx
#import plotly.express as px
import requests

url_path = "https://data.cityofnewyork.us/resource/h9gi-nx95.json"
data = pd.read_json(url_path)
new_data = pd.to_datetime(data['crash_date','crash_time']) 
st.write(new_data)
d = pd.json_normalize(data.json())

st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a streamlit dashboard that can be used to analyze motorvehicle collisions in NYC.")





           


  
