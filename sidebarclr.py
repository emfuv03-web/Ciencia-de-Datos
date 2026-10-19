import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

clash_link = ("https://raw.githubusercontent.com/emfuv03-web/ClashRoyaleplayers/refs/heads/main/players.csv ")
st.header("Data Descriptions")
st.header("JUGADORES DE CLASH ROYALE ")
sidebar = st.sidebar
sidebar.title("BUSCAR UN JUGADOR ")

clash_data = pd.read_csv(clash_link)
st.dataframe(clash_data)
jugador = sidebar.text_input('Nombre')
if sidebar.button ('Buscar'):
     st.dataframe(nombre)
     
if jugador:
    nombre = clash_data[clash_data["name"].str.contains(jugador, case = False, na = False)]

if enseñamela:
     
     st.write(f"Search name : {jugador}")
    
    enseñamela = st.checkbox("Mostrar tabla de jugadores")

















