
import streamlit
import pandas as pd
import requests


streamlit.header("State Testing Historical Data Set")
data = pd.read_csv("https://knowi.com/api/data/ipE4xJhLBkn8H8jisFisAdHKvepFR5I4bGzRySZ2aaXlJgie?entityName=States%20Testing%20Historical&exportFormat=csv")
data = data.set_index("date")

date_state_df = data.groupby(by=["date", "State"]).sum()

date_selected = streamlit.multiselect("Choose a date:", list(data.index))
date_to_show = date_state_df.drop(columns=["grade"])
date_to_show = date_state_df.loc[date_selected]

streamlit.dataframe(date_to_show.style.highlight_max(axis=0))


  
