import streamlit as st
import pandas as pd

names_link = "https://raw.githubusercontent.com/emfuv03-web/ClashRoyaleplayers/refs/heads/main/players.csv"
names_data = pd.read_csv(names_link)

st.title("streamlit and pandas")
st.dataframe(names_data)