import pandas as pd
import numpy as np
import streamlit as st

map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50, 50] + [18.916422228717217, -97.02435314647327],
    columns=['lat', 'lon'])

st.title("San Francisco Map")
st.header("Using Streamlit an Mapbox")
st.map(map_data)