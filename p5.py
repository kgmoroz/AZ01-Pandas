import pandas as pd

df = pd.read_csv('product_data.csv')

df.drop(287, axis=0, inplace=True)

print(df)