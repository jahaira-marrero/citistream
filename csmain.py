import streamlit
import pandas as pd
import requests
streamlit.header("State Testing Historical Data Set")

data = pd.read_csv("https://knowi.com/api/data/ipE4xJhLBkn8H8jisFisAdHKvepFR5I4bGzRySZ2aaXlJgie?entityName=States%20Testing%20Historical&exportFormat=csv")
data = data.set_index('State')
streamlit.multiselect("Choose your filters:", list(data.index)
streamlit.dataframe(data)

