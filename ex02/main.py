'''1. В файле находится N натуральных чисел, записанных через пробел.
Среди чисел не хватает одного, чтобы выполнялось условие 
A[i] - 1 = A[i-1]. Найдите это число'''

import os
from tokenize import Triple
path1 = os.path.join('PythonSem05', 'ex02', 'input1.txt')
with open(path1, 'r') as my_file:
    data1 = my_file.read()
data1 = data1.split()
print(data1)


data1 = [1, 2, 4, 5, 6]
for i in range(1, len(data1)):
    if data1[i]-data1[i-1] != 1:
        print(data1[i-1]+1)

print('вариант решения 2:')

x = tuple(filter(lambda i: (data1[i]-data1[i-1]) != 1, range(1, len(data1))))
print(x[0]+1)


# path = os.path.join('PythonHW05', 'ex02', 'output.txt')

# with open(path, 'a') as f:
#     for item in xArrSum:
#         f.write("%s" % item)
