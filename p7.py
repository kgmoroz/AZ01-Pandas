import pandas as pd

# Чтение CSV-файла в DataFrame
df = pd.read_csv('product_data.csv')

# Удалить строки с пропущенными значениями
df.dropna(inplace=True)

# Отфильтровать строки, содержащие "Подвесной светильник" в столбце name
filtered_df = df[df['name'].str.contains('Подвесной светильник')]

# Вычислить среднюю цену для отфильтрованных строк
average_price = filtered_df['price'].mean()

# Вывести среднюю цену
print(f'Средняя цена всех товаров вида "Подвесной светильник": {average_price:.2f}')

df.to_csv('product_data_2.csv', index=False)