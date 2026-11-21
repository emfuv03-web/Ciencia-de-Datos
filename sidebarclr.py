import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

clash_link = "https://raw.githubusercontent.com/emfuv03-web/ClashRoyaleplayers/refs/heads/main/players.csv"

sidebar = st.sidebar
sidebar.title("BUSCAR UN JUGADOR")
st.header("Data Descriptions")
st.header("JUGADORES DE CLASH ROYALE")


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(clash_link, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    return data


clash_data = load_data(1000)

enseñamela = st.checkbox("Mostrar tabla de jugadores")
if enseñamela:
    st.dataframe(clash_data)

jugador = sidebar.text_input("Nombre")
if sidebar.button("Buscar"):
    if jugador:
        nombre = clash_data[
            clash_data["name"].str.contains(jugador, case=False, na=False, regex=False)
        ]
        st.write(f"Search name: {jugador}")
        st.dataframe(nombre)
    else:
        st.warning("Escribe el nombre de un jugador")

copas_de_jugadores = sidebar.slider(
    "Copas mínimas",
    min_value=int(clash_data["trophies"].min()),
    max_value=int(clash_data["trophies"].max())
)
filtro_copas = clash_data[clash_data["trophies"] >= copas_de_jugadores]
st.write("Copas")
st.dataframe(filtro_copas)

lista_de_jugadores = sidebar.selectbox(
    "Seleccion de jugador", clash_data["name"].dropna().unique()
)
st.write(f"Selected Option: {lista_de_jugadores!r}")
jugador_seleccionado = clash_data[clash_data["name"] == lista_de_jugadores]
st.dataframe(jugador_seleccionado)

expan = sidebar.expander("Seleccionar nivel de experiencia")
experiencia = expan.radio(
    "Selecciona el nivel de experiencia:", clash_data["explevel"].dropna().unique()
)
nivel_del_jugador = clash_data[clash_data["explevel"] == experiencia]
st.write("Nivel")
st.dataframe(nivel_del_jugador)

arenas = clash_data["name_arena"].dropna().value_counts()
fig, ax = plt.subplots()
ax.bar(arenas.index, arenas.values)
st.header("Tabla de barras de arenas")
st.pyplot(fig)

paises = clash_data["name_pais"].dropna().value_counts()
fig2, ax2 = plt.subplots()
ax2.bar(paises.index, paises.values)
st.header("Tabla de barras de países")
st.pyplot(fig2)

niveles = clash_data["explevel"].dropna().value_counts()
fig3, ax3 = plt.subplots()
ax3.pie(niveles.values, labels=niveles.index, autopct='%1.1f%%')
st.header("Gráfica de pastel de niveles de experiencia")
st.pyplot(fig3)

st.header("Orizaba (Oriyork), Veracruz")
map_data = pd.DataFrame(
    np.random.randn(1, 2) / [900, 900] + [18.850376904197645, -97.10364925510632],
    columns=['lat', 'lon']
)
st.map(map_data)
st.header("Hecho por Elias Martinez Flores")
st.header("Matricula ZS26004617")
sidebar.write("Hecho por Elias Martinez Flores")
sidebar.write("Matricula ZS26004617")