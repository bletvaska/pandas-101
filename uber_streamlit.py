import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    data_load_state = st.markdown('Nahrávam dataset...')
    df = pd.read_csv(
        'data/uber-clean.csv.gz', 
        index_col=0,
        parse_dates=['dt']
    )
    data_load_state.markdown('Nahrávam dataset... Nahraté (z cache).')
    return df

st.title('Uber Pickups in NYC')
st.image('images/uber.jpg')

st.markdown('Pozrieme sa bližšie na jazdy spoločnosti [Uber](https://www.uber.com).')

'Dataset, ktorý použijeme na túto aplikáciu si je možné stiahnuť z portálu [Kaggle](https://www.kaggle.com).'

st.header('Nahratie datasetu')

df = load_data()

if st.checkbox('Zobraziť dáta') is True:
    df


'## Prehľad jázd za deň'

day = 1
month = 1
year = 2014

filter_date = (
    (df['dt'].dt.year == year)
    & (df['dt'].dt.month == month)
    & (df['dt'].dt.day == day)
)


