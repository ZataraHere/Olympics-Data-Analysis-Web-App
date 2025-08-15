import streamlit as st
import pandas as pd

import helper
import preprocess

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocess.preprocess(df, region_df)

st.sidebar.image('https://e7.pngegg.com/pngimages/1020/402/png-clipart-2024-summer-olympics-brand-circle-area-olympic-rings-olympics-logo-text-sport.png')
st.sidebar.title("Olympics Analysis")
st.sidebar.image('https://wallpapers.com/images/hd/men-s-running-event-olympic-sports-ofh5ckbutl16vpaz.jpg')
user_select = st.sidebar.radio(
    'select an option',
    ('Medal Tally', 'Overall Analysis','Country Wise Analysis','Overall Analysis')
)


#st.dataframe(df)

if user_select == 'Medal Tally':

    st.sidebar.header("Medal Tally")
    years,country = helper.country_years_list(df)

    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(selected_year, selected_country, df)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title('Overall Tally')
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medal Tally in "+str(selected_year)+" Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country+"'s Overall Performance")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country+"'s Overall Performance in "+str(selected_year)+" Olympics")

    st.table(medal_tally)