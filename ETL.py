import pandas as pd 
import pymysql
import streamlit as st

def connect_database():
    try :
        timeout = 10
        conn = pymysql.connect(
            charset ="utf8mb4",
            connect_timeout = timeout,
            cursorclass=pymysql.cursors.DictCursor,
            host = st.secrets["DB_HOST"],
            user = st.secrets["DB_USER"],
            password = st.secrets["DB_PASSWORD"],
            port=int(st.secrets["DB_PORT"]),
            database=st.secrets["DB_NAME"],
            write_timeout=timeout,
        )
        return conn
    except pymysql.Error as e :
        print("Database Connection Failed : " , e)

    # function to fetch Data
def fetch_data(cursor , db_name , table_name) :
        cursor.execute("Select * from {}.{}".format(db_name,table_name))
        return cursor.fetchall()
    
def load_jotstar_data(cursor):
        # Fetching data from jotstar_db.content_consumption table
        data_1 = fetch_data(cursor , "jotstar_db", "content_consumption")
        content_consumption_df = pd.DataFrame(data_1 , columns = ["user_id" , "device_type" , "total_watch_time_mins"])
        
        #fetching data from jotstar_db.contents table
        data_2 = fetch_data(cursor , "jotstar_db", "contents")
        contents_df = pd.DataFrame(data_2 , columns = ["content_id" , "content_type" , "language" , "genre" , "run_time"])
        
        #fetching data from jotstar_db.subscribers table
        data_3 = fetch_data(cursor , "jotstar_db", "subscribers")
        subscribers_df = pd.DataFrame(data_3 , columns = ["user_id" , "age_group" , "city_tier" , "subscription_date" , "subscription_plan" , "last_active_date" , "plan_change_date" , "new_subscription_plan"])
        
        return content_consumption_df , contents_df , subscribers_df

    # function to display the table information
def General_info(table_name):
        print(" ")
        table_name.info()
        return table_name.describe()  , table_name.isnull().sum()

    # Function for converting datatypes
def converting_datatypes(table_name , column_name):
        table_name[column_name] = pd.to_datetime(table_name[column_name])
        return table_name[column_name]

    # filling missing values in subscribers_df
def fill_missing_value(table_name , column_name) :
        if table_name[column_name].dtype == "str":
            new_value = table_name[column_name].mode()[0]
            return table_name.fillna({column_name : new_value} , inplace= True)
        else:
            new_value = table_name[column_name].median()
            return table_name.fillna({column_name : new_value} ,inplace=True)
        
def clean_data_Jotstar(cursor):
        content_consumption_df, contents_df, subscribers_df = load_jotstar_data(cursor)
        # Converting date columns to datetime format
        column_name = ["subscription_date" , "last_active_date" , "plan_change_date"]
        for i in range(len(column_name)): 
            converting_datatypes(subscribers_df , column_name[i]) # Function Calling
        
        # filling missing values in subscribers_df
        column_names_missing_value = ['plan_change_date' , 'last_active_date' , "new_subscription_plan"]
        for i in range(len(column_names_missing_value)):
            fill_missing_value(subscribers_df , column_names_missing_value[i])

        return content_consumption_df , contents_df , subscribers_df



    # ---------------------------------------------------------------------------------

    # fetching data from liocinema_db.content_consumption table
def load_liocinema_data(cursor):
        data4 = fetch_data(cursor , "liocinema_db", "content_consumption") # Function_calling
        content_consumption_df_2 = pd.DataFrame(data4 , columns = ["user_id" , "device_type" , "total_watch_time_mins"])
        
        data5 = fetch_data(cursor , "liocinema_db", "contents") # Function_calling
        contents_df_2 = pd.DataFrame(data5 , columns = ["content_id" , "content_type" , "language" , "genre" , "run_time"])
        
        data6 = fetch_data(cursor , "liocinema_db", "subscribers") # Function_calling
        subscribers_df_2 = pd.DataFrame(data6 , columns = ["user_id" , "age_group" , "city_tier" , "subscription_date" , "subscription_plan" , "last_active_date" , "plan_change_date" , "new_subscription_plan"])
        
        return content_consumption_df_2 , contents_df_2 , subscribers_df_2

def clean_data_Liocinema(cursor):
        content_consumption_df_2, contents_df_2, subscribers_df_2 = load_liocinema_data(cursor)
        # Converting date columns to datetime format
        column_name = ["subscription_date" , "last_active_date" , "plan_change_date"]
        for i in range(len(column_name)): 
            converting_datatypes(subscribers_df_2 , column_name[i]) # Function Calling
        
        # filling missing values in subscribers_df
        column_names_missing_value = ['plan_change_date' , 'last_active_date' , "new_subscription_plan"]
        for i in range(len(column_names_missing_value)):
            fill_missing_value(subscribers_df_2 , column_names_missing_value[i])

        return content_consumption_df_2 , contents_df_2 , subscribers_df_2

if __name__ == "__main__":
    conn = connect_database()
    if conn is not None :
        cursor = conn.cursor()