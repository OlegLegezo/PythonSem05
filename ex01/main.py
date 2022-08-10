print('lambda - короткая функция с выражением (анонимная функция) спрятать мелкое действие')


def f(x): return x**2


print(f(2))

print('map - применение функции к каждому элементу списка')


def f(x):
    return x**2


my_list = [1, 2, 3, 4, 50]

for item in my_list:
    print(f(item), end=' ')

# короткая запись:


def new_f(x): return x**2


res = list(map(new_f, my_list))
# вместо list можно tuple/set
print(res)


# короткая запись тернарный оператор:
def new_f(x): return True if (x > 10) else False


res = list(map(new_f, my_list))
# вместо list можно tuple/set
print(res)

print('включения list comprehension - генерируем что-то и пишем')
my_list = [i for i in range(20) if i > 10]
print(my_list)

# res=[input() for i in range(5)]
# print(res)


print('filter - работает аналогично map')
myStartList = [23, 22, 9, 1, 2, 123]
my_list = list(filter(lambda x: x > 10, myStartList))
print(my_list)



print('zip - берет одинаковые и помещает в кортеж')
a=['a','b','c','d']
b=[1,2,3]
my_list=list(zip(a,b))
print(my_list)



print('получаем словарь')
my_list=dict(zip(a,b))
print(my_list)


print('делаем enumerate - просто нумеруем (удобная индексация)')
a=['a','b','c','d']
my_list=list(enumerate(a))
print(my_list)
