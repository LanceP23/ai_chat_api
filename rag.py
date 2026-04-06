import pandas as pd 
import chromadb

client = chromadb.Client()
collection = client.create_collection("engineers")
jobs_collection = client.create_collection("jobs")

df = pd.read_csv("./data/engineers.csv")
df2 = pd.read_csv("./data/jobs.csv")

chunks = []
job_chunks = []

salary_average = df['salary'].mean()
df['salary'] = df['salary'].fillna(salary_average)
df['specialization'] = df['specialization'].fillna('unknown')
df['years_experience'] = df['years_experience'].fillna(df['years_experience'].mean())
df['age'] = df['age'].fillna(df['age'].mean())



for index, row in df.iterrows():
    chunks.append(f"{row['name']}, is {row['age']} years old, specializes in {row['specialization']}, has {row['years_experience']} years experience and earns {row['salary']}")
for chunk in chunks:
    print(chunk)

for index, row in df2.iterrows():
    job_chunks.append(f"{row['title']}, {row['company']}, requires {row['required_experience']} years, skills: {row['required_skills']}, salary: {row['salary_range']}, location: {row['location']}")

collection.add(
    documents=chunks,
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)

jobs_collection.add(
    documents = job_chunks,
    ids=[f"job_chunks_{i}" for i in range(len(job_chunks))]
)


def query_rag(question):

    results = collection.query(
        query_texts=[question],
        n_results = 5
    )
    job_results = jobs_collection.query(
    query_texts=[question],
    n_results=3
    )
    relevant_chunks = results["documents"][0] + job_results["documents"][0]
    context = "\n".join(relevant_chunks)
    print("Retrieved chunks:", relevant_chunks)
    return context
