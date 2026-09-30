import streamlit as st
import pandas as pd
import datetime

#give user the current date
today = datetime.date.today()
today_date = st.date_input('current date', today)
st.success('current date: ´%s´' %(today_date))

titanic_data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")

#display the content of data set if checkbox is true
st.header("DataSet")
agree = st.checkbox("show DataSet overview ? ")

if agree:
    st.dataframe(titanic_data)

selected_town = st.radio("Select Embark Town",
titanic_data['embark_town'].unique())
st.write("selected Embark Town:", selected_town)

optionals = st.expander("Optional Configurations", True)

fare_min = optionals.slider(
    "Minimum Fare", 
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
fare_max = optionals.slider(
    "Maximum Fare", 
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) &
                           (fare_min <= titanic_data['fare'])]
st.write(f"Number of records With fare Between{fare_min} and{fare_max}: {subset_fare.shape[0]}")

st.dataframe(subset_fare)