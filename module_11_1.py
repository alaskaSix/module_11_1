import requests
import pandas as pd
import numpy as np

'''Requests — библиотека для работы с HTTP-запросами. Она позволяет получать данные с различных веб-сайтов и API.'''

response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.status_code == 200:
    data = response.json()
    print("Первые 3 записи:", data[:3])
else:
    print("Ошибка при запросе данных:", response.status_code)


'''Pandas — это библиотека для анализа данных, позволяет легко работать с таблицами и выполнять различные манипуляции над данными.'''

data = pd.read_csv("weather_data.csv")  # Убедитесь, что файл есть в вашей директории
print("Первые 5 строк данных:\n", data.head())
print("Статистика по температуре:\n", data['Temperature'].describe())
grouped_data = data.groupby('City')['Temperature'].mean()
print("Средняя температура по городам:\n", grouped_data)

'''NumPy — библиотека для работы с многомерными массивами и выполнения сложных математических операций.'''

array = np.random.rand(5)
print("Массив случайных чисел:", array)
print("Среднее значение:", np.mean(array))
print("Массив, умноженный на 2:", array * 2)