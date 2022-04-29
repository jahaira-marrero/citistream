
import streamlit
import pandas as pd
import requests


streamlit.header("State Testing Historical Data Set")
data = pd.read_csv("https://knowi.com/api/data/ipE4xJhLBkn8H8jisFisAdHKvepFR5I4bGzRySZ2aaXlJgie?entityName=States%20Testing%20Historical&exportFormat=csv")
#data = data.set_index("State")

date_state_df = data.groupby(by=["date"]).sum()

date_selected = streamlit.multiselect("Choose a date:", list(date_state_df))
date_to_show = data.loc[date_selected]

streamlit.dataframe(date_to_show)


  
