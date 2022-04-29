import streamlit
import pandas as pd
import requests
streamlit.header("State Testing Historical Data Set")

data = requests.get("https://knowi.com/api/data/ipE4xJhLBkn8H8jisFisAdHKvepFR5I4bGzRySZ2aaXlJgie?entityName=States%20Testing%20Historical&exportFormat=csv")
data_normalzed = pd.json_normalize(data.json())

streamlit.dataframe(data_normalized)
