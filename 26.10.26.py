#float bool str list int
#float
# int - ЦЕЛОЧИСЛЕННЫЕ
# bool-логика
# str-строк
#a='jui'

#list-список []
#a=[1,2,3,4,5]
#a=[0]=10

#set-множество
#s={1,2,2,3,4,4,3,3}

#tuple-кортеж
#s=(1,2,3,4,5)

#dict-словарик
#s={ключ:значения}
#s={'key':'value','key1':'value'}
#print(s)

#none-ничего

# a=10
# b=a
# a=20
# print(a,b)

# a=[1,2,3]
# b=a
# a.append(10)    [1,2,3,10] [1,2,3,10]

#print(10,20,30,sep='',end='')
#\n-перенос на другую строку \t-табулиция

#input-ввод в консоль
#a=input

# + - / * //-целочисленное   %- с остатком
#print(10%4)

# > <  >= <= == != - false/true

#in not in
#print(10 in [,2,3,4,10])   true

#and or not-логичесие операторы
#логическое и - and *
#or логическое или,+
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 1
#not- инверсия
# not true-false
# not false-true

#неявное/явное приведение типов
#неявное

#float>int>bool
#s=20/2   10.0   #float
#s=20 + 2.0 float

# s=10 + True
# print(s)

#явное приведение
# a=int(float('10.4'))
# print(a+1)
#  a=int(input)
#  print(a+10)

 # a,b=10,30
 # print(a,b)

# a= int(input())
# b = int(input())
# c=a
# a=b
# b=c
#print(a,b)

#print(129 // 10 % 10)

# x = int(input())
# print(1<x<10, 1<x and x<10)

#условные операторы
#bool
#s = bool(0)
# s = bool()
# print(s)

#if else elif
# is_rain = False
# if is_rain:
#     print('зонт')
# else:
#     print('не берем')

# x = 10
# if x > 10:
#     print('x > 10')
# elif x > 5 :
#     print('5 < 10 <=10')


# x = int(input())
# if x % 2==0:
#     print('чет')
# else:
#     print('неч')


# a = int(input())
# b = int(input())
# c = int(input())
# if a==b==c:
#     print('ravn')
# elif a==b or a == c or b==c:
#     print('ravnobedr')
# else:
#     print('razn')

#цикл while
# x=0
# while x < 10:
#     x += 1
# print(x)
# x = 3
# while x > 0:
#     print(x)
#     x -=1

# x=0
# is_run=True
# while is_run:
#     g=int(input())
#     if g== 10:
#         is_run=False
#     print(x)
#     x +=1

x=int(input())
a=1
summ=0
while a<=x:
    summ+=7*a
    a +=1
print(summ)

