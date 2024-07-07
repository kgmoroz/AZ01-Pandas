import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Claire', 'David', 'Eve'],
    'Age': [25, 30, 27, 35, 28],
    'City': ['London', 'Paris', 'Berlin', 'Moscow', 'Chicago']
}

df = pd.DataFrame(data)
print(df)