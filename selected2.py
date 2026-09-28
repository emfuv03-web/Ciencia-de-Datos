import streamlit as st
import pandas as pd
st.title ("Titanic Dataset")

data =pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.dataframe(data)
selected_age = st.selectbox("Select Age", data['age'].unique()) 

st.write(f"Selected Option: {selected_age!r}")
filtered_data_age = data[data['age'] == selected_age]

st.dataframe(filtered_data_age)