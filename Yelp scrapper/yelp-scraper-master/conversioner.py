import pandas as pd 
df = pd.read_json('output.json')
print(df.head())
df.to_csv('converted.csv')