import datetime

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

date = st.date_input('**Vyber dátum:**', datetime.date(2014, 1, 1))

filter_date = (
    (df['dt'].dt.year == date.year)
    & (df['dt'].dt.month == date.month)
    & (df['dt'].dt.day == date.day)
)

df_filtered = df.loc[ filter_date, : ]

data = df_filtered.groupby( df_filtered['dt'].dt.hour )['passengers'].count()
profit = df_filtered.loc[ filter_date, 'fare' ].sum()

f"Zisk: **${profit:.2f}**"
st.bar_chart(data)


f'## Nástupy na mape zo dňa {date}'

hour_to_filter = st.slider('Vyber hodinu', 0, 23, 12)

st.map(df_filtered, 
       latitude='pickup_latitude', 
       longitude='pickup_longitude',
       # zoom=4
)
