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
st.write ("Copas")
st.dataframe(filtro_copas)

lista_de_jugadores = sidebar.selectbox("Seleccion de jugador", clash_data['name'].unique()) 

st.write(f"Selectes Option: {lista_de_jugadores!r}")
lista_de_jugadores = clash_data[clash_data['name'] == lista_de_jugadores]

st.dataframe(lista_de_jugadores)

experiencia = sidebar.radio(
    "Selecciona el nivel de experiencia:",
    clash_data["explevel"].unique()
)

nivel_del_jugador = clash_data[
    clash_data["explevel"] == experiencia
]

st.write("Nivel")
st.dataframe(nivel_del_jugador)

