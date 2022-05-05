import datetime
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
#import plotly.express as px
import requests

url= "https://data.cityofnewyork.us/resource/h9gi-nx95.json"

st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a streamlit dashboard that can be used to analyze motorvehicle collisions in NYC.")

st.cache(persist=True)
data = pd.read_json(url)
data.crash_date = data.crash_date.str.split('T').str[0]

data.crash_time = data.crash_time.apply(lambda x: x.strftime('%H:%M'))
data.crash_time = data.crash_time.dt.time

data.dropna(subset = ['latitude', 'longitude'], inplace=True)

st.write(data)

st.header("Where are the most people injured in NYC?")
injured_people = st.slider("Number if persons injured in vehicle collisions", 0,10)
st.map(data.query("number_of_persons_injured >= @injured_people")[["latitude", "longitude"]].dropna(how="any"))

st.header("How many collisions occur during a given time of day?")
hour = st.slider("Hour to look at", 0, 23)
#data = data[data['crash_time'].dt.hour == hour]



st.markdown("Vehicle collisions between %i:00 and %i:00" %(hour, (hour +1) % 24))

midpoint = (np.average(data['latitude']), np.average(data['longitude']))
st.write(pdk.Deck(
           map_style="mapbox://styles/mapbox/light-v9",
           initial_view_state={
                      "latitude": midpoint[0],
                      "longitude": midpoint[1],
                      "zoom": 11,
                      "pitch": 50,
           },
           layers = [
                      pdk.Layer(
                                 "HexagonLayer",
                                 data=data[['crash_time', 'latitude', 'longitude']],
                                 get_position=['latitude', 'longitude'],
                                 radius=100,
                                 extruded=True,
                                 pickable = True,
                                 elevation_scale=4,
                                 elevation_range=[1,1000],
                      ),
           ],
))





           


  
