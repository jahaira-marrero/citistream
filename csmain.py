
import streamlit
import pandas as pd
import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import count, desc, col, max, struct, round, mean, min, expr, substring, to_date, sum
from pyspark.sql import functions as F
import matplotlib.pyplot as plts

spark= SparkSession.builder.appName('Spark_app').getOrCreate()


streamlit.header("State Testing Historical Data Set")
# data = pd.read_csv("https://knowi.com/api/data/ipE4xJhLBkn8H8jisFisAdHKvepFR5I4bGzRySZ2aaXlJgie?entityName=States%20Testing%20Historical&exportFormat=csv")
# data = data.set_index("date")

# date_state_df = data.groupby(by=["date", "State"]).sum()
# date_selected = streamlit.multiselect("Choose a date:", list(data.index))
# date_to_show = date_state_df.loc[date_selected]

# #streamlit.line_chart(data(columns=["State", "date"]))

# streamlit.dataframe(date_to_show.style.highlight_max(axis=0))


  
