import streamlit as st
st.title("Mi Primera App con Streamlit")
sidebar = st.sidebar
sidebar.title("Esta es la barra lateral. ")
sidebar.write("aqui an los elementos de la entrada. ")
st.header("Informacion sobre el conjunto de datos ")
st.header("descripcion de los datos")

st.write("""
Este es un simple ejemplo de una app para predecir

¡esta app predice mis datos!

""")
