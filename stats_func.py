import numpy as np
# Создаем массив чисел
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Вычисляем среднее значение
mean_value = np.mean(data)

# Находим медиану
median_value = np.median(data)

# Вычисляем стандартное отклонение
std_dev = np.std(data)
#Выводим результат расчетов:
# Печатаем результаты
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_dev)