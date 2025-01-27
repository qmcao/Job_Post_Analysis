# dashboard.py
import streamlit as st
import mysql.connector
import pandas as pd
from dotenv import load_dotenv
import os


# Connect to MySQL
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database="linkedin_jobs"
    )

if __name__ == "__main__":
    load_dotenv()
    # Dashboard title
    st.title("📊 Data Science Jobs Dashboard")

    # Sidebar filters
    st.sidebar.header("Filters")
    location = st.sidebar.selectbox(
        "Location",
        ["All"] + list(pd.read_sql("SELECT DISTINCT job_location FROM jobs", get_connection())['job_location'])
    )

    # Query based on filters
    query = "SELECT job_title, company, job_location, first_seen FROM jobs"
    if location != "All":
        query += f" WHERE job_location = '{location}'"

    # Fetch data
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()

    # Display results
    st.write(f"**{len(df)} jobs found in {location if location != 'All' else 'all locations'}**")
    st.dataframe(df.head(10))

    # Visualizations
    st.subheader("Top Job Titles")
    title_counts = df['job_title'].value_counts().head(10)
    st.bar_chart(title_counts)

    st.subheader("Top Companies")
    company_counts = df['company'].value_counts().head(10)
    st.bar_chart(company_counts)