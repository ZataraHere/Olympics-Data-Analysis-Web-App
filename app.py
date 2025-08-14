import streamlit as st
import pandas as pd

import helper
import preprocess

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocess.preprocess(df, region_df)

user_select = st.sidebar.radio(
    'select an option',
    ('Medal Tally', 'Overall Analysis','Country Wise Analysis','Overall Analysis')
)


st.dataframe(df)

if user_select == 'Medal Tally':
    medal_tally = helper.medal_tally(df)
    st.dataframe(medal_tally)