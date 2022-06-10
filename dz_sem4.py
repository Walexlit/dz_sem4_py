'''
# Ввычислить число пи, (использовать Ряд Нилаканта или любой другой вариант расчета числа Пи 
# примеры расчетов можно посмотреть по ссылке ==> http://www.swsys.ru/files/2018-2/409-413.pdf ) c заданной точностью d
'''

# d = int(input('введите число '))
# pi = 0
# i = 0
# while i < d:
#     pi += (1/(16**i))*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
#     i += 1
# print(round(pi, d))


'''
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''
# n=int(input('введите число '))
# def Mnoj(n):
#     l = []
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             l.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         l.append(n)
#     return l
# print(Mnoj(n))


'''
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
[1,2,3,5,1,5,3,10]=>[1,2,3,5,10]
'''

# l=[1,2,3,5,1,5,3,10]
# l2=[]
# for i in l:
#     if i not in l2:
#         l2.append(i)
# print(l)
# print(l2)

'''
# Задана натуральная степень n. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени пример записи в файл при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0 при n=2 ==> 27x^2 + 95x + 79 = 0
'''


# from ntpath import join
# from random import randint, random
# n = int(input('введите степень '))
# l = []
# nul = '= 0'

# for i in range(0, n+1):
#     l.append(randint(0, 100))
#     if n >= 1:
#         l.append('x')
#     if n >= 2:
#         l.append('^')
#     if n >= 2:
#         l.append(n)

#     if n >= 1:
#         l.append('+')
#     n -= 1

# l = str(l)
# l = ''.join(l)


# def repl(x):
#     return x.replace(",", "").replace("'", "").replace(" ", "").replace("[", " ").replace("]", " ")

# l= repl(l)

# for k in l:
#     if k == '+':
#         l = l.replace('+', ' + ')
# l += nul
# print(l)


# # data = open('pol_2.txt', 'a')
# # data.writelines(l)
# # data.close()


'''
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов. (нужно два полинома сложить. Файлы взять благодаря предыдущему заданию)'''

# from re import L
# from select import select


# path = 'pol_1.txt'
# x =open (path,'r')
# for poly_1 in x:
#     a=poly_1
# x.close()
# print(a)
# #                    убераем знаки
# def dels (x):
#     return  x.replace(' ','').replace('x','').replace('^','').replace('+',' ').replace('=0','')

# a=dels(a)
# a=a.split()


# #                    убераем степень в а 
# j=0
# lis=[]      
# for f in a:
#     if j<len(a)-2:
#         f=f[:-1]
#         j+=1
#     lis.append(f)

  

# path = 'pol_2.txt'
# y =open (path,'r')
# for poly_2 in y:
#     b=poly_2
# y.close()
# print(b)


# b=dels(b)
# b=b.split()

# #               убираем степень в многочлене б
# j=0
# lis_2=[]      
# for f in b:
#     if j<len(b)-2:
#         f=f[:-1]
#         j+=1
#     lis_2.append(f)



# #                         переводим в int и складываем
# lis=(list(map(int, lis)))
# lis_2=(list(map(int, lis_2)))
# lis_3=(list(map(sum,zip(lis,lis_2))))



# #                              добавляем знаки
# c=[]
# nul = '= 0'
# n= len(lis_3)




# for i in lis_3:
#     if n >= 1:
#         c.append(i)
#     if n>=2:    
#         c.append('x')
#     if n >= 3:
#         c.append('^')
#     if n >= 3:
#         c.append(n-1)

#     if n >= 2:
#         c.append('+')
#     n -= 1
# c = str(c)
# c = ''.join(c)


# def repl(x):
#     return x.replace(",", "").replace("'", "").replace(" ", "").replace("[", " ").replace("]", " ")

# c= repl(c)

# for k in c:
#     if k == '+':
#         c = c.replace('+', ' + ')
# c += nul
# print(c)


# # data = open('sum.txt', 'a')
# # data.writelines(c)
# # data.close()
