import streamlit as st
import pandas as pd 
st.title("hello persona random")
dataframe = pd.read_csv("https://raw.githubusercontent.com/emfuv03-web/ClashRoyaleplayers/refs/heads/main/players.csv")
st.dataframe(dataframe)
st.write("by emfuv03")
