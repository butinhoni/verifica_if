import pandas as pd

def getPlanilha():
    df = pd.read_csv(r'http://docs.google.com/spreadsheets/d/1ah6gftR6jQJBZhcQZoz5-MEMVbN4fHt2zWJmT7mMWuA/export?format=csv')
    df = df.dropna(subset=['Nome'])
    return(df)

getPlanilha()