import streamlit as st
import pandas as pd

# to run your streamlit website, go into terminal and input:
# streamlit run main.py

df = pd.read_csv("earthquakes_dataset.csv")
df['DATE'] = pd.to_datetime(df['DATE'], format='%m/%d/%Y')
df['YEAR'] = pd.DatetimeIndex(df['DATE']).year
years = list(range(1965, 2017))

st.header('Significant Earthquakes 1965-2016')
st.text("An earthquake is the shaking of the surface of the Earth caused by a sudden release \n"
        "of energy that produces seismic waves. This is normally the result of tectonic \n"
        "plates moving past one-another and building up friction, which is eventually \n"
        "released. This site allows you to choose a year and see all significant earthquakes \n"
        "that were recorded and their locations on the map.")

year = st.selectbox('Choose year', ['All Years (1965-2016)'] + years)

if year == 'All Years (1965-2016)':
    st.dataframe(df)
    st.map(df)
else:
    year_df = df.loc[df['YEAR'] == year]
    st.dataframe(year_df)
    st.map(year_df)
    
