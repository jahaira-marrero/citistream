
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
data = pd.read_json(url, convert_dates=['crash_date', 'crash_time'])
data.dropna(subset = ['latitude', 'longitude'], inplace=True)

st.write(data)

st.header("Where are the most people injured in NYC?")
injured_people = st.slider("Number if persons injured in vehicle collisions", 0,19)
st.map(data.query("number_of_persons_injured >= @injured_people")[["latitude", "longitude"]].dropna(how="any"))




           


  
