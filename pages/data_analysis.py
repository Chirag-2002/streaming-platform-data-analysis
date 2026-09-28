import streamlit as st
from ETL import (
    connect_database,
    clean_data_Jotstar,
    clean_data_Liocinema
)
from Analysis import (
    KPI,
    total_users_growth_trends,
    content_library_comparison,
    user_demographics,
    watch_time_analysis
)


conn = connect_database()
cursor = conn.cursor()

content_consumption, content, subscribers = clean_data_Jotstar(cursor)

content_consumption_2, content_2, subscribers_2 = clean_data_Liocinema(cursor)

st.title("OTT Platform Analysis Dashboard")
kpi = KPI(content_consumption , content , subscribers , content_consumption_2 , content_2 , subscribers_2)
total_user_jotstar , total_user_liocinema = kpi.total_users()
total_paid_jotstar , total_paid_liocinema = kpi.total_paid_users()
total_content_jotstar , total_content_liocinema = kpi.total_contents()
total_watch_time_jotstar , total_watch_time_liocinema = kpi.total_watch_time()
avg_watch_time_jotstar , avg_watch_time_liocinema = kpi.avg_watch_time()

kpi_tab = st.radio("Select the ott platform for KPI : " , ["Jotstar" , "Liocinema"])
col1 , col2 , col3 , col4 , col5 = st.columns(5)

if kpi_tab == "Jotstar":
    with col1:
        st.metric(
            label = "Total Users (Jotstar)",
            value = f"{total_user_jotstar : ,}"
        )
    with col2:
        st.metric(
            label = "Total Paid Users",
            value = f"{total_paid_jotstar : ,}"
        )
    with col3:
        st.metric(
            label="Total Content",
            value = f"{total_content_jotstar : ,}"
        )
    with col4:
        st.metric(
            label="Total watch time",
            value = f"{total_watch_time_jotstar : ,}"
        )
    with col5 :
        st.metric(
            label = "Avg watch time",
            value = f"{avg_watch_time_jotstar:,}"
        )
        
if kpi_tab == "Liocinema":
    with col1:
        st.metric(
            label = "Total Users",
            value = f"{total_user_liocinema: ,}"
        )
    with col2:
        st.metric(
            label = "Total Paid Users",
            value = f"{total_paid_liocinema : ,}"
        )
    with col3:
        st.metric(
            label="Total Content",
            value = f"{total_content_liocinema : ,}"
        )
    with col4:
        st.metric(
            label="Total watch time",
            value = f"{total_watch_time_liocinema : ,}"
        )
    with col5 :
        st.metric(
            label = "Avg watch time",
            value = f"{avg_watch_time_liocinema:,}"
        )

col1 , col2 = st.columns(2)
with col1:
    st.subheader("User growth trend  ")
    fig = total_users_growth_trends(subscribers , subscribers_2)
    st.plotly_chart(fig , use_container_width=True)
with col2:
    st.subheader("Content Comparison ")
    fig = content_library_comparison(content , content_2)
    st.plotly_chart(fig ,use_container_width=True)

col3 , col4 = st.columns(2)
with col3:
    st.subheader("User Demographics")
    fig =  user_demographics(subscribers , subscribers_2)   
    st.plotly_chart(fig , use_container_width=True)
with col4:
    st.subheader("Watch Time analysis")
    fig = watch_time_analysis(content_consumption , subscribers , content_consumption_2 , subscribers_2)
    st.plotly_chart(fig , use_container_width=True)