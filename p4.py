import pandas as pd

df = pd.read_csv('product_data.csv')

df['Currency'] = 'RUB'

print(df)

df.drop('Currency', axis=1, inplace=True)

print(df)