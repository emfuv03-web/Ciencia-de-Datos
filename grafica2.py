import streamlit as st
import pandas as pd 
import matplotlib.pyplot as ptl

titanic_link = 'https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv'

titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data)
st.header("Data Descriptions")

fig2, ax2 = ptl.subplots()
y_pos = titanic_data['class']
x_pos = titanic_data['fare']

ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Class")
ax2.set_xlabel("Fare")
ax2.set_title('¿Cuanto pagaron las clases del Titanic')

st.header("grafica de barras del titanic")
st.pyplot(fig2)
