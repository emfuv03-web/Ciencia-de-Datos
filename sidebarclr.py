import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

clash_link = ("https://raw.githubusercontent.com/emfuv03-web/ClashRoyaleplayers/refs/heads/main/players.csv ")
st.header("Data Descriptions")
st.header("JUGADORES DE CLASH ROYALE ")
sidebar = st.sidebar
sidebar.title("BUSCAR UN JUGADOR ")
@st.cache_data
def load_data(nrows):
    data = pd.read_csv("https://raw.githubusercontent.com/emfuv03-web/ClashRoyaleplayers/refs/heads/main/players.csv ", nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

clash_data = load_data(1000)
enseñamela = st.checkbox("Mostrar tabla de jugadores")
if enseñamela: 
     st.dataframe(clash_data)



jugador = sidebar.text_input('Nombre')    
if jugador:
     st.write(f"Search name : {jugador}")

nombre = clash_data[clash_data["name"].str.contains(jugador, case = False, na = False)]

if sidebar.button ('Buscar'):
     st.dataframe(nombre)

copas_de_jugadores = sidebar.slider(
    "Copas", 
    min_value=int(clash_data['trophies'].min()),
    max_value=int(clash_data['trophies'].max())

)
filtro_copas = clash_data[clash_data["trophies"] == copas_de_jugadores]
st.dataframe(filtro_copas)
