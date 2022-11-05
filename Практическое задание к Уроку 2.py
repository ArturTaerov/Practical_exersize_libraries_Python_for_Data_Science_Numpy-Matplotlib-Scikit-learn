import numpy as np
import pandas as pd

# Задание 1
# Импортируйте библиотеку Numpy и дайте ей псевдоним np.
# Создайте массив Numpy под названием a размером 5x2, то есть состоящий из 5
# строк и 2 столбцов. Первый столбец должен содержать числа 1, 2, 3, 3, 1, а
# второй - числа 6, 8, 11, 10, 7. Будем считать, что каждый столбец - это
# признак, а строка - наблюдение. Затем найдите среднее значение по каждому
# признаку, используя метод mean массива Numpy. Результат запишите в массив
# mean_a, в нем должно быть 2 элемента.

A = np.array([[1, 2, 3, 3, 1],[6, 8, 11, 10, 7]])
print(A)
A = A.transpose()
print(A)
mean_a = [np.mean(A.transpose()[i]) for i in range(2)]
print(mean_a)

# Задание 2
# Вычислите массив a_centered, отняв от значений массива “а” средние значения
# соответствующих признаков, содержащиеся в массиве mean_a. Вычисление должно
# производиться в одно действие. Получившийся массив должен иметь размер 5x2.

a_centered = A - mean_a
print(a_centered)

# Задание 3
# Найдите скалярное произведение столбцов массива a_centered. В результате
# должна получиться величина a_centered_sp. Затем поделите a_centered_sp на 
# N-1, где N - число наблюдений.

a_centered_sp = a_centered.transpose()[0].dot(a_centered.transpose()[1].copy()\
                                              .transpose())
print(a_centered_sp)
print(a_centered_sp/(len(A.transpose()[0])-1))


# Задание 1
# Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм
# authors со столбцами author_id и author_name, в которых соответственно
# содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
# Затем создайте датафрейм book cо столбцами author_id, book_title и price, в
# которых соответственно содержатся данные: [1, 1, 1, 2, 2, 3, 3],
# ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий',
# 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
# [450, 300, 350, 500, 450, 370, 290].

data1 = {"author_id": [1, 2, 3], "author_name": ['Тургенев', 'Чехов', \
                                                 'Островский']}
authors = pd.DataFrame(data1)
print(authors)
data2 = {"author_id": [1, 1, 1, 2, 2, 3, 3], "book_title": ['Отцы и дети', \
         'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', \
         'Гроза', 'Таланты и поклонники'], "price": [450, 300, 350, 500, 450, \
                                                     370, 290]}
books = pd.DataFrame(data2)
print(books)

# Задание 2
# Получите датафрейм authors_price, соединив датафреймы authors и books по полю
# author_id.

authors_price = pd.merge(authors, books) 
print(authors_price)

# Задание 3
# Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью
# самыми дорогими книгами.

top5 = authors_price.sort_values(by='price', ascending = False)
print(top5.head(5))

# Задание 4
# Создайте датафрейм authors_stat на основе информации из authors_price.
# В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора, минимальная,
# максимальная и средняя цена на книги этого автора.
 
df = authors_price.groupby("author_name")
min_price = df.agg({"price": "min"}).rename(columns={'price': 'min_price'})
max_price = df.agg({"price": "max"}).rename(columns={'price': 'max_price'})
mean_price = df.agg({"price": "mean"}).rename(columns={'price': 'mean_price'})
authors_stat = pd.concat([min_price, max_price, mean_price], axis=1)
print(authors_stat)

