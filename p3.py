import pandas as pd

df = pd.read_csv('World-happiness-report-2024.csv')

#print(df) # вывод всего датафрейма
#print(df.head(10)) # вывод первых 10 строк
#print(df.tail(10)) # вывод последних 10 строк
#print(df.columns) # вывод названий столбцов
#print(df.dtypes) # вывод типов данных
#print(df.info()) # вывод информации
#print(df.describe()) # вывод описательной статистики
#print(df.shape) # вывод размера
#print(df.isnull().sum()) # вывод пропущенных значений
#print(df.nunique()) # вывод уникальных значений
#print(df['Country name'].unique()) # вывод уникальных значений
#print(df['Regional indicator'].unique()) # вывод уникальных значений
#print(df['Regional indicator'].value_counts())
#print(df.loc[56]) # вывод строки с индексом 56
print(df[df['Healthy life expectancy'] > 0.7])