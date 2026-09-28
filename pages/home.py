import streamlit as st
from ETL import connect_database, clean_data_Jotstar, clean_data_Liocinema
from Analysis import total_users_growth_trends

conn = connect_database()
cursor = conn.cursor()
content_consumption , content , subscribers = clean_data_Jotstar(cursor)
content_consumption_2 , content_2 , subscribers_2 = clean_data_Liocinema(cursor)

st.title("Analytics for OTT Platform (Jotstar Vs Liocinema)")
st.header("Overview")
st.write("This application provides analytics for the OTT platforms Jotstar and Liocinema. You can explore the data, perform analysis, and visualize insights from the content consumption, content, and subscriber data.")
st.subheader("Data")
nav = st.radio("Select the things you want to see", ["Data", "Analysis"])
if nav == "Data":
    st.write("Some glimpse of data . For more details, please go to the Data page.")
    st.subheader("Jotstar Data Overview")
    st.dataframe(content_consumption.head())
    st.subheader("Liocinema Data Overview")
    st.dataframe(content_consumption_2.head())
elif nav == "Analysis":
    st.write("Some glimpse of analysis . For more details, please go to the Analysis page.")
    st.subheader("User Growth Trend")
    fig = total_users_growth_trends(subscribers, subscribers_2)
    st.plotly_chart(fig , use_container_width=True)