import streamlit as st

st.set_page_config(page_title="Analytics for OTT Platform (Jotstar Vs Liocinema)", layout="wide")

home = st.Page(
    "pages/home.py",
    title = "Home"
)

data = st.Page(
    "pages/data.py",
    title = "Data Overview"
)

analysis = st.Page(
    "pages/data_analysis.py",
    title = "Analysis"
)


pg = st.navigation(
    [home, data, analysis],
    position="sidebar"
)

pg.run()

