import pandas as pd 


df = pd.read_csv("./data/engineers.csv")

def get_top_paid(df):

    top_10 = df.groupby('specialization')['salary'].idxmax()
    top_earners = df.loc[top_10]
    top_earners.to_csv("./data/top_earners.csv", index =False)

     

def get_all_engineers():
    return df.to_dict('records')
