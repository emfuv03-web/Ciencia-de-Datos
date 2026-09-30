import pandas as pd
import streamlit as st
import matplotlib.pyplot as ptl

titanic_link = 'https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv'

titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data)
st.header("Data Descriptions")

fig, ax = ptl.subplots()
ax.hist(titanic_data.fare)
st.header("Histograma del Titanic")
st.pyplot(fig)
