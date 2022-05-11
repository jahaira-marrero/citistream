import datetime
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
#import plotly.express as px
import requests

st.title("Citibike Trips")


def get_sblist():
           with my_cnx.cursor() as my_cur:
             my_cur.execute("select * from trips limit 100")
             return my_cur.fetchall()
                      

if streamlit.button("Get Trips"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_sblist()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)
           



  
