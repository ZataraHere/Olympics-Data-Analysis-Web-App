import streamlit as st
import pandas as pd

import helper
import preprocess

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocess.preprocess(df, region_df)

st.sidebar.title("Olympics Analysis")
st.sidebar.image('https://e7.pngegg.com/pngimages/1020/402/png-clipart-2024-summer-olympics-brand-circle-area-olympic-rings-olympics-logo-text-sport.png')
user_select = st.sidebar.radio(
    'select an option',
    ('Medal Tally', 'Overall Analysis','Country Wise Analysis','Overall Analysis')
)


st.dataframe(df)

if user_select == 'Medal Tally':

    st.sidebar.header("Medal Tally")
    years,country = helper.country_years_list(df)

    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.medal_tally(df)
    st.dataframe(medal_tally)