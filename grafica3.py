import streamlit as st
import pandas as pd
import matplotlib.pyplot as ptl


titanic_link = 'https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv'

titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data)
st.header("Data Descriptions")

fig3, ax3 = ptl.subplots()

ax3.scatter(titanic_data.age,titanic_data.fare)
ax3.set_xlabel("Edad")
ax3.set_ylabel("Tarifa")

st.header("Grafica de dispercion del titanic")
st.pyplot(fig3)
