import pandas as pd
import streamlit as st

df = pd.read_excel('data_wisata_bogor_hyperlink_tereh_final.xlsx')

df_clean = df.drop_duplicates(subset=['nama_tempat_wisata'])

df_clean["harga_tiket"] = pd.to_numeric(df["harga_tiket"], errors="coerce")

df = df_clean[df_clean["harga_tiket"] > 0]

st.write(df.reset_index())