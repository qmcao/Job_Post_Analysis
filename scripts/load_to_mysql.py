from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd


if __name__ == "__main__":
    
    
    job_posting_path = "D:\project\Job_Posting_Analysis\data\job_postings.csv"
    job_skill_path = "D:\project\Job_Posting_Analysis\data\job_skills.csv"
    
    job_posting = pd.read_csv(job_posting_path)
    job_skill = pd.read_csv(job_skill_path)
    
    # Drop missing column for simplicity
    job_skill.dropna(inplace=True)
    job_posting.dropna(inplace=True)
    
    
    load_dotenv()  # Load environment variables from .env file
    # MySQL credentials (store these in .env)
    USER = os.getenv("MYSQL_USER")
    PASSWORD = os.getenv("MYSQL_PASSWORD")
    HOST = "127.0.0.1"
    DATABASE = "linkedin_jobs"

    engine = create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}")
    # Load data into MySQL table
    job_posting.to_sql('jobs', con=engine, if_exists='replace', index=False)
    print("Data loaded to MySQL!")
    
    # Load 
    job_skill.to_sql('jobs_skill', con=engine, if_exists='replace', index=False)
    print("Data loaded to MySQL!")