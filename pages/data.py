import streamlit as st
from ETL import *


conn = connect_database()
cursor = conn.cursor()
content_consumption , content , subscribers = clean_data_Jotstar(cursor)
content_consumption_2 , content_2 , subscribers_2 = clean_data_Liocinema(cursor)


st.title("Details about the data used for analysis")
st.write("This is a simple Streamlit app to display details about the data used for analysis.")

data = st.radio("Select the platform from which you have to see the data" ,["Jotstar" , "Liocinema"] )

st.write("Select the data you want to see :")
content_check = st.checkbox("content")
content_consumption_check = st.checkbox("content consumption")
subscribers_check = st.checkbox("subscribers")

if data == "Jotstar":
    st.subheader("Jotstar Data")
    st.write("This database contains detailed data on content, subscribers, and content consumption for the Jotstar platform, enabling insights into content, user behavior, and platform performance trends.")
    if content_check:
        st.markdown(
        """
        ### Content Data
        
        Purpose: This table provides detailed information about the content available on Jotstar platform, enabling analysis of content diversity, genre popularity, and runtime patterns.
        - content_id: Unique identifier for each content item on the platform (e.g., CJSMHITHR850d1, CJSMHIACTf59cd).
        - content_type: Type of content (e.g., Movie, Series).
        - language: Language in which the content is available (e.g., Hindi, English).
        - genre: Genre of the content (e.g., Romance, Action, Drama).
        - run_time: Duration of the content in minutes (e.g., 120, 150).
        """
        )
        st.dataframe(content)
    if content_consumption_check:
        st.markdown(
    """
    ### 3. Content Consumption
    Purpose: This table captures user-level content consumption data, enabling analysis of total watch time, device preferences, and engagement trends.
    - user_id: Unique identifier for each subscriber (e.g., UIDJS6dc2a37454b).
    - device_type: Type of device used to consume content (e.g., Mobile, TV, Tablet).
    - total_watch_time (mins): Total time spent watching content in minutes (e.g., 13598, 2105).
    """
        )
        st.dataframe(content_consumption)
    if subscribers_check:
        st.markdown(
    """
    ## 2. subscribers
    Purpose: This table captures demographic and subscription details for Jotstar users, enabling insights into subscriber acquisition, upgrades, downgrades, and inactivity patterns.
    - user_id: Unique identifier for each subscriber (e.g., , UIDJS7215b8ce306, UIDJSa5e350fa952).
    - age_group: Age group of the subscriber (e.g., 18-24, 25-34).
    - city_tier: City category of the subscriber (e.g., Tier 1, Tier 2, Tier 3).
    - subscription_date: The date when the user subscribed Jotstar (formatted as YYYY-MM-DD).
    - subscription_plan:  The initial subscription plan chosen by the user at the time of subscribing (e.g., Free, VIP, Premium).
    - last_active_date: The most recent date the user interacted with the platform. For inactive users, this column captures the last recorded date of activity, and for active users, it is NULL (formatted as YYYY-MM-DD).
    - plan_change_date: Date when the user’s subscription plan was last updated (formatted as YYYY-MM-DD).
    - new_subscription_plan: The updated subscription plan, if applicable, reflecting any upgrades or downgrades (e.g., upgrade to VIP/Premium, downgrade to Free/VIP).

    """
        )
elif data == "Liocinema":
    st.subheader("Liocinema Data")
    st.write("This database contains detailed data on content, subscribers, and content consumption for the LioCinema platform, enabling insights into content, user behavior, and platform performance trends.")
    if content_check:
        st.write("Description is same as Jotstar")
        st.dataframe(content_2)
    if content_consumption_check:  
        st.write("Description is same as Jotstar")
        st.dataframe(content_consumption_2)
    if subscribers_check:
        st.write("Description is same as Jotstar")
        st.dataframe(subscribers_2)
