import datetime
import streamlit
import pandas as pd
import numpy as np
import pydeck as pdk
import snowflake.connector
#import plotly.express as px
import requests

streamlit.title("Citibike Trips")
df = pd.read_csv('https://raw.githubusercontent.com/jahaira-marrero/citistream/main/cbtrips.csv')

if streamlit.button('See Raw Data'):
        streamlit.write(df)

           



  
