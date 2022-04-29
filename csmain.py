
import streamlit
import pandas as pd
import requests


streamlit.header("State Testing Historical Data Set")
data = pd.read_csv("https://knowi.com/api/data/ipE4xJhLBkn8H8jisFisAdHKvepFR5I4bGzRySZ2aaXlJgie?entityName=States%20Testing%20Historical&exportFormat=csv")

for col in data.columns:
  streamlit.write(col)
  
streamlit.write(data.groupby(by=["date"]).sum())
 

streamlit.multiselect("Choose your filters:", list(data.index))

streamlit.dataframe(data)


  
