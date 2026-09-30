# OTT Platform Data Analysis — JioStar vs LioCinema

A complete end-to-end **Python-based data analysis and Streamlit dashboard project** comparing OTT platform data from **JioStar** and **LioCinema**.

This project covers the complete data analytics lifecycle — from database connection and ETL to data cleaning, analysis, visualization, cloud database migration, Git/GitHub management, secrets management, and Streamlit Cloud deployment.

---

## 📌 Project Overview

The objective of this project is to analyze and compare user behavior, subscriptions, content consumption, watch time, demographics, and content characteristics across two OTT platforms:

* **JioStar**
* **LioCinema**

The project uses relational databases hosted on **Aiven MySQL**, Python for ETL and analysis, Pandas for data manipulation, Plotly for interactive visualization, and Streamlit for the dashboard.

### Key Questions Explored

* How many users does each platform have?
* How many paid users are there?
* How are users growing over time?
* What are the subscription trends?
* Which content types and genres are consumed more?
* How does watch time vary between platforms?
* What are the demographic characteristics of users?
* How do users behave across devices?
* How do content libraries differ?
* What insights can be derived from subscription and consumption behavior?

---

# 🏗️ Project Architecture

```text
                    ┌───────────────────────┐
                    │      Aiven MySQL      │
                    │                       │
                    │    jotstar_db         │
                    │    liocinema_db       │
                    └───────────┬───────────┘
                                │
                                │ PyMySQL
                                ▼
                    ┌───────────────────────┐
                    │        ETL.py         │
                    │                       │
                    │  • Connect database  │
                    │  • Extract data       │
                    │  • Transform data     │
                    │  • Clean data         │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │      Analysis.py      │
                    │                       │
                    │  • KPI calculations  │
                    │  • User analysis     │
                    │  • Watch-time        │
                    │  • Content analysis  │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │      Streamlit        │
                    │       Dashboard       │
                    │                       │
                    │ • Home                │
                    │ • Data                │
                    │ • Data Analysis       │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   Streamlit Cloud     │
                    │      Deployment       │
                    └───────────────────────┘
```

---

# 🛠️ Technology Stack

| Technology      | Purpose                              |
| --------------- | ------------------------------------ |
| Python          | ETL, data cleaning and analysis      |
| Pandas          | Data manipulation and transformation |
| NumPy           | Numerical operations                 |
| Plotly          | Interactive data visualization       |
| Streamlit       | Dashboard and web application        |
| MySQL           | Relational database                  |
| PyMySQL         | Python–MySQL connection              |
| Aiven           | Cloud-hosted MySQL                   |
| Git             | Version control                      |
| GitHub          | Source-code hosting                  |
| Streamlit Cloud | Application deployment               |
| SQL             | Data extraction and querying         |

---

# 📂 Project Structure

```text
Python_based_Analysis/
│
├── .streamlit/
│   └── secrets.toml
│
├── pages/
│   ├── home.py
│   ├── data.py
│   └── data_analysis.py
│
├── ETL.py
├── Analysis.py
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── Input_files/
    └── ...
```

### File Responsibilities

### `ETL.py`

Responsible for:

* Connecting to MySQL
* Extracting data
* Loading tables into Pandas DataFrames
* Data type conversion
* Missing-value handling
* Preparing cleaned datasets

### `Analysis.py`

Contains reusable analytical functions such as:

* KPI calculations
* Total users
* Paid users
* Total content
* Total watch time
* Average watch time
* User growth analysis
* Content library comparison
* Demographic analysis
* Watch-time analysis

### `app.py`

Main Streamlit application entry point.

### `pages/home.py`

Dashboard landing page and overview.

### `pages/data.py`

Displays data and datasets used by the application.

### `pages/data_analysis.py`

Contains analytical dashboard components, KPIs, charts, comparisons, and interactive analysis.

### `.streamlit/secrets.toml`

Stores sensitive database credentials locally.

**This file must never be committed to GitHub.**

---

# 🗄️ Database Structure

The project uses two databases:

```text
jotstar_db
liocinema_db
```

Both databases contain similar logical tables.

### Main Tables

```text
content_consumption
contents
subscribers
```

---

## `content_consumption`

Contains user-level content consumption information.

Example fields:

```text
user_id
device_type
total_watch_time_mins
```

---

## `contents`

Contains content metadata.

Example fields:

```text
content_id
content_type
language
genre
run_time
```

---

## `subscribers`

Contains subscriber information.

Example fields:

```text
user_id
age_group
city_tier
subscription_date
subscription_plan
last_active_date
plan_change_date
new_subscription_plan
```

---

# 🔄 ETL Process

The ETL process is implemented in `ETL.py`.

ETL stands for:

```text
Extract
Transform
Load
```

---

## 1. Extract

PyMySQL is used to connect Python to MySQL.

```python
import pymysql
import pymysql.cursors
```

The database connection is created using:

```python
pymysql.connect(
    host=...,
    user=...,
    password=...,
    port=...,
    database=...
)
```

---

## 2. Fetch Data

A reusable function is used to retrieve data from different tables:

```python
def fetch_data(cursor, db_name, table_name):
    query = f"SELECT * FROM `{db_name}`.`{table_name}`"
    cursor.execute(query)
    return cursor.fetchall()
```

This allows the same function to be used for both databases.

---

# 🧹 Data Cleaning

The project performs several data-cleaning operations.

## Date Conversion

Subscription-related columns are converted to Pandas datetime format:

```python
pd.to_datetime(table_name[column_name])
```

Columns include:

```text
subscription_date
last_active_date
plan_change_date
```

This allows date-based analysis and time-series calculations.

---

## Missing Values

Missing values are handled using:

* Mode for categorical columns
* Median for numerical columns

Example:

```python
new_value = table_name[column_name].mode()[0]
```

or:

```python
new_value = table_name[column_name].median()
```

---

# 📊 Data Analysis

The analytical layer is implemented in `Analysis.py`.

The project calculates several KPIs.

## User KPIs

Examples:

```text
Total Users
Total Paid Users
User Growth
```

## Content KPIs

Examples:

```text
Total Content
Content Type Distribution
Genre Distribution
Language Distribution
```

## Watch-Time KPIs

Examples:

```text
Total Watch Time
Average Watch Time
Watch Time by Device
Watch Time by Content
```

---

# 📈 Interactive Visualization

The project uses **Plotly** for interactive data visualization.

Plotly is used to create:

* Line charts
* Bar charts
* Horizontal bar charts
* Comparative visualizations
* Interactive charts
* Hover-based data exploration

Example:
