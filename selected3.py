import streamlit as st
import pandas as pd
st.title ("Titanic Dataset")

data =pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.dataframe(data)
selected_class = st.selectbox("Select Class", data['class'].unique()) 

st.write(f"Selectes Option: {selected_class!r}")
filtered_data_class = data[data['class'] == selected_class]

st.dataframe(filtered_data_class)