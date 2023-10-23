import streamlit as st
import pandas as pd

st.set_page_config(
    'Livianu - ECOP06'
    'https://http2.mlstatic.com/D_NQ_NP_928746-MLB47621207721_092021-O.webp')

st.title(('Palmeiras não tem mundial'))
st.subheader('51 é pinga')

esportes = pd.read_csv(
    'https://github.com/MainakRepositor/Datasets/raw/master/GeneralEsportData.csv',
    encoding='latin-1')

st.dataframe(esportes)