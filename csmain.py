
import streamlit
import pandas as pd
import requests


streamlit.header("State Testing Historical Data Set")
data = pd.read_csv("https://knowi.com/api/data/ipE4xJhLBkn8H8jisFisAdHKvepFR5I4bGzRySZ2aaXlJgie?entityName=States%20Testing%20Historical&exportFormat=csv")
#data_df = spark.read.format('csv').option('inferSchema', True).option('header', True).load("https://knowi.com/api/data/ipE4xJhLBkn8H8jisFisAdHKvepFR5I4bGzRySZ2aaXlJgie?entityName=States%20Testing%20Historical&exportFormat=csv")
data = data.set_index('date')
#date_data = data\.groupby(pd.TimeGrouper('M'))\.agg({'combined':''.join})
streamlit.multiselect("Choose your filters:", list(data.index))
#streamlit.dataframe(data)
streamlit.dataframe(data)

