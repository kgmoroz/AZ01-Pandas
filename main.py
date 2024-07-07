import pandas as pd

# ЗАДАНИЕ 1
# Чтение CSV-файла в DataFrame
df = pd.read_csv('World-happiness-report-2024.csv')

# вывод первых 5 строк
print(df.head())

# вывод информации о данных
print(df.info())

# вывод статистического описания
print(df.describe())


# ЗАДАНИЕ 2
# Чтение CSV-файла в DataFrame
df = pd.read_csv('dz.csv')

# группировка по городам и вычисление средней зарплаты
group = df.groupby('City')['Salary'].mean()
print(group)