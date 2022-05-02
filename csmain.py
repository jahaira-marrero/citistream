
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdx
import plotly.express as px
# from sodapy import Socrata
import requests


# client = Socrata("data.cityofnewyork.us", None)
# results = client.get("h9gi-nx95", limit=2000)
# results_df = pd.DataFrame.from_records(results)
# DATA_URL = requests.get("https://data.cityofnewyork.us/resource/h9gi-nx95.json")

def load_data(nrows):
    data = pd.json_normalized(DATA_URL.json(), nrows  = nrows, parse_dates=[['CRASH_DATE', 'CRASH_TIME']])
    return data

data = load_data(100000)

st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a streamlit dashboard that can be used to analyze motorvehicle collisions in NYC."
st.text(data)

           


  
