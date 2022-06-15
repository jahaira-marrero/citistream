import datetime
import streamlit
import pandas as pd
import numpy as np
import pydeck as pdk
import snowflake.connector
#import plotly.express as px
import requests

streamlit.title("Citibike Trips")

def get_citi_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from trips limit 10")
        return my_cur.fetchall()

if streamlit.button('Get List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_citi_list()
#     my_cnx.close()
    streamlit.dataframe(my_data_rows)



# df = pd.read_csv('https://raw.githubusercontent.com/jahaira-marrero/citistream/main/cbtrips.csv')

# if streamlit.button('See Raw Data'):
#         streamlit.write(df)

          
# st.cache(persist=True)
# def load_data(nrows):
#     data = pd.read_csv(url, nrows = nrows, parse_dates=[['CRASH DATE', 'CRASH TIME']])
#     data.dropna(subset = ["LATITUDE", "LONGITUDE"], inplace=True)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis = 'columns', inplace=True)
#     data.rename(columns={'crash date_crash time': 'date/time'}, inplace=True)
#     return data

# data = load_data(100000)
# original_data = data
# st.write(data)


# st.header("Where are the most people injured in NYC?")
# injured_people = st.slider("Number of persons injured in vehicle collisions", 0, 14)
# st.map(data.query("number of injured persons>= @injured_people")[["latitude", "longitude"]].dropna(how="any"))

# st.header("How many collisions occur during a given time of day?")
# hour = st.slider("Hour to look at", 0, 23)
# data = data[data['date/time'].dt.hour == hour]


# st.markdown("Vehicle collisions between %i:00 and %i:00" %(hour, (hour +1)))

# midpoint = (np.average(data['latitude']), np.average(data['longitude']))
# st.write(pdk.Deck(
#            map_style="mapbox://styles/mapbox/light-v9",
#            initial_view_state={
#                       "latitude": midpoint[0],
#                       "longitude": midpoint[1],
#                       "zoom": 11,
#                       "pitch": 50,
#            },
#            layers = [
#                       pdk.Layer(
#                                  "HexagonLayer",
#                                  data=data[['date/time', 'latitude', 'longitude']],
#                                  get_position=['latitude', 'longitude'],
#                                  radius=100,
#                                  extruded=True,
#                                  pickable = True,
#                                  elevation_scale=4,
#                                  elevation_range=[1,1000],
#                       ),
#            ],
# ))

# st.subheader("Breakdown by minute between %i:00 and %i:00" %(hour, (hour +1) %24))
# filtered = data[
#     (data['date/time'].dt.hour >= hour) & data['date/time'].dt.hour < (hour + 1)
# ]
# hist = np.histogram(filtered['date/time'].dt.minute, bins=60, range=(0,60))[0]
# chart_data = pd. DataFrame({'minute': range(60), 'crashes': hist})
# fig = px.bar(chart_data, x='minute', y='crashes', hover_data=['minute', 'crashes'], height = 400)
# st.write(fig)


# st.header("Top 5 Dangerous Collision Streets by Type")
# select = st.selectbox('Affected Type:', ['Pedestrians', 'Cyclists', 'Motorists'])

# if select == 'Pedestrians':
#            st.write(original_data.query("injured_pedestrians >= 1")[["on_street_name","injured_pedestrians"]].sort_values(by=['injured_pedestrians'], ascending=False).dropna(how='any')[:5])





  
