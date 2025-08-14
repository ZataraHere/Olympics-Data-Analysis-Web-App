import streamlit as st
import pandas as pd

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

user_select = st.sidebar.radio(
    'select an option',
    ('Medal Tally', 'Overall Analysis','Country Wise Analysis','Overall Analysis')
)