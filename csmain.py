
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdx
#import plotly.express as px
import requests

url_path = requests.get("https://data.cityofnewyork.us/resource/h9gi-nx95.json")
#data = pd.read_json(url_path)
d = pd.json_normalize(url_path.json())

st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a streamlit dashboard that can be used to analyze motorvehicle collisions in NYC.")
st.write(d)





           


  
