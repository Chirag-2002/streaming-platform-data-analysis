import pandas as pd
import plotly.express as px 

# Now i will calculate the KPI as follows for both the platforms and then compare them to see which platform is performing better.:
"""
1) Total Users 
2) Total Watch time
3) Avg Watch time 
4) Total contents a
5) Paid Users 
6) Active & inactive users
"""
class KPI:
    def __init__(self , content_consumption, content, subscribers , content_consumption_2, content_2, subscribers_2):
        self.content_consumption = content_consumption
        self.content = content
        self.subscribers = subscribers
        self.content_consumption_2 = content_consumption_2
        self.content_2 = content_2
        self.subscribers_2 = subscribers_2
    def total_users(self):
        total_users_jotstar = self.content_consumption['user_id'].nunique()
        total_users_liocinema = self.content_consumption_2['user_id'].nunique()
        return total_users_jotstar, total_users_liocinema
    def total_watch_time(self):
        total_watch_time_jotstar = self.content_consumption['total_watch_time_mins'].sum()
        total_watch_time_liocinema = self.content_consumption_2['total_watch_time_mins'].sum()
        return total_watch_time_jotstar , total_watch_time_liocinema
    def avg_watch_time(self):
        avg_watch_time_jotstar = self.content_consumption['total_watch_time_mins'].mean()
        avg_watch_time_liocinema = self.content_consumption_2['total_watch_time_mins'].mean()
        return avg_watch_time_jotstar , avg_watch_time_liocinema
    def total_contents(self):
        total_contents_jotstar = self.content['content_id'].nunique()
        total_contents_liocinema = self.content_2['content_id'].nunique()
        return total_contents_jotstar , total_contents_liocinema 
    def total_paid_users(self):
        total_paid_users_jotstar = self.subscribers[self.subscribers["new_subscription_plan"].isin(["Premium", "VIP"])]['user_id'].nunique()
        total_paid_users_liocinema = self.subscribers_2[self.subscribers_2["new_subscription_plan"].isin(["Premium", "VIP"])]['user_id'].nunique()
        return total_paid_users_jotstar , total_paid_users_liocinema


# now we will start visualizing the data to see which platform is performing better. 
# We will use matplotlib to visualize the data.

""" 1. Total Users & Growth Trends
● What is the total number of users for LioCinema and Jotstar, and how do they
compare in terms of growth trends (January–November 2024)? """

def total_users_growth_trends(subscribers, subscribers_2):
    jotstar = subscribers.groupby('subscription_date')['user_id'].nunique().reset_index()
    liocinema = subscribers_2.groupby('subscription_date')['user_id'].nunique().reset_index()
    
    jotstar["Platform"] = "Jotstar"
    liocinema["Platform"] = "liocinema"
    
    combined = pd.concat(
        [jotstar , liocinema],
        ignore_index=True
    )
    
    fig = px.line(
        combined , 
        x = "subscription_date",
        y = "user_id",
        color = "Platform",
        title = "Total Users and Growth Trends (Jan - Nov 2024)",
        labels = {
            "user_id" : "Total Users",
            "subscription_date":"Date"
        }
    )
    
    fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Users"
)
    return fig

""" 2. Content Library Comparison
● What is the total number of contents available on LioCinema vs. Jotstar? How do
they differ in terms of language and content type? """

def content_library_comparison(content, content_2):
    jotstar_content = content.groupby(["content_type" , "language"])['content_id'].nunique().reset_index().nlargest(10, 'content_id')
    liocinema_content = content_2.groupby(["content_type" , "language"])['content_id'].nunique().reset_index().nlargest(10, 'content_id')
    
    jotstar_content["Platform"] = "Jotstar"
    liocinema_content["Platform"] = "liocinema"
    
    for df in [jotstar_content , liocinema_content] :
        df["content_demographic"] = (
            df['content_type'].astype(str) + 
            "-" + df['language'].astype(str)
        )
    combined_df = pd.concat(
        [jotstar_content , liocinema_content],
        ignore_index=True
    )
    
    fig = px.bar(
        combined_df , 
        x = "content_id",
        y="content_demographic",
        orientation="h",
        color="Platform",
        title = "Content Library Comparison",
        labels = {
            "content_id" : "Content",
            "Demographic" : "content_type - language"
        }
    )
    
    fig.update_layout(
        xaxis_title = "Content",
        yaxis_title = "content_demographic"
    )
    
    
    return fig

""" 3. User Demographics
● What is the distribution of users by age group, city tier, and subscription plan for each
platform? """

def user_demographics(subscribers, subscribers_2):
    jotstar_user_demographics = subscribers.groupby(["age_group" , "city_tier" , "new_subscription_plan"])['user_id'].nunique().reset_index().nlargest(10, 'user_id')
    liocinema_user_demographics = subscribers_2.groupby(["age_group" , "city_tier" , "new_subscription_plan"])['user_id'].nunique().reset_index().nlargest(10, 'user_id')   
    
    jotstar_user_demographics["Platform"] = "Jotstar"
    liocinema_user_demographics["Platform"] = "liocinema"
    
    for df in [jotstar_user_demographics , liocinema_user_demographics] :
        df["user_demographic"] = (
            df['age_group'].astype(str) + 
            "-" + df['city_tier'].astype(str) +
            "-" + df['new_subscription_plan'].astype(str)
        )
    combined_df = pd.concat(
        [jotstar_user_demographics , liocinema_user_demographics],
        ignore_index=True
    )
    
    fig = px.bar(
        combined_df , 
        x = "user_id",
        y="user_demographic",
        orientation="h",
        color="Platform",
        title = "User Demographics",
        labels = {
            "user_id" : "User",
            "user_demographic" : "age_group-city_tier-new_subscription_plan"}
    )
    
    fig.update_layout(
        xaxis_title = "User",
        yaxis_title = "user_demographic"
    )
    
    
    return fig

""" 5. Watch Time Analysis
● What is the average watch time for LioCinema vs. Jotstar during the analysis period?
How do these compare by city tier and device type? """
def watch_time_analysis(content_consumption, subscribers, content_consumption_2, subscribers_2):
    result_jotstar = pd.merge(content_consumption[["user_id" , "device_type" , "total_watch_time_mins"]] , subscribers[["user_id" , "city_tier"]] , on="user_id" , how="inner")
    jotstar_watch_time_analysis = result_jotstar.groupby(["device_type","city_tier"])["total_watch_time_mins"].mean().reset_index().nlargest(10, 'total_watch_time_mins')

    result_liocinema = pd.merge(content_consumption_2[["user_id" , "device_type" , "total_watch_time_mins"]] , subscribers_2[["user_id" , "city_tier"]] , on="user_id" , how="inner")
    liocinema_watch_time_analysis = result_liocinema.groupby(["device_type","city_tier"])["total_watch_time_mins"].mean().reset_index().nlargest(10, 'total_watch_time_mins')
    
    jotstar_watch_time_analysis["Platform"] = "Jotstar"
    liocinema_watch_time_analysis["Platform"] = "Liocinema"
    
    for df in [jotstar_watch_time_analysis , liocinema_watch_time_analysis]:
        df["Device_type & City Tier"] = (
            df["device_type"] + "-" +df["city_tier"]
        )
    combined_df = pd.concat(
        [jotstar_watch_time_analysis , liocinema_watch_time_analysis],
        ignore_index=True
    )
    
    fig = px.bar(
        combined_df , 
        x = "total_watch_time_mins",
        y = "Device_type & City Tier",
        orientation="h",
        color="Platform",
        title = "Watch time analysis",
        labels = {
            "total_watch_time_mins" : "Watch Time",
            "Device_type & City Tier" : "Device Type - City Tier"
        }
    )
    
    fig.update_layout(
        xaxis_title = "Watch Time",
        yaxis_title = "Device_type & City_Tier"
    )
    return fig

