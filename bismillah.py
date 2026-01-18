import pandas as pd
import streamlit as st

df = pd.read_csv('data_wisata_bogor_finalz.csv')
st.write(df)