import string
import math
# 1
def first(n):
    n=int (n)
    rez = 0
    for i in range(1, n + 1):
        r = 0
        if n % i == 0:
            for d in range(1, n + 1):

                if i % d == 0:
                    r = r + 1
        if r == 2:
            rez += i

    return rez

# 2
def secondd(n):#кол-во нечетных чисел идущих до этого числа больше трех
    n=int(n)
    rez = 0
    for i in range(1, n + 1):
        if i % 2 != 0 and i > 3:
            rez += 1
    return rez

#3
def suminstr():#произведение числа сумма цифор которого меньше самого числа например 14
    ch = int(input())
    chsum=sum([int(c) for c in str(ch)])
    #n=int(input())
    #a=[int(d) for d in str(n)]
    #print(sum(a))
    rez=1
    for i in  range (1,ch):
        if ch%i==0:
            prov=sum([int(t) for t in str(i)])
            if chsum>prov:
                rez=rez*i
    return(rez)

#4
def countrus(s):
    count = 0
    for i in range(0, len(s)):
        if s[i] >= 'А' and s[i] <= 'я':
            count += 1
    return count

#5
def ispolindrom(s):
    flag = True

    for i in range(0, len(s) // 2):
        if (s[i] != s[len(s) - i - 1]):
            flag = False
    return flag

#6
def datafinder(s):#найти дату например рвлорылорваылоравол ловырловырлор лорывлоарлрывалорваы ловырдлардлывор 20 мая 2040 ловырлавоырлвыаорлвыа
    countblank = 0
    for a in range(0, len(s)):
        if (s[a] == ' '):
            countblank += 1
    s = s.split(' ')
    for i in range(0, countblank):
        if s[i] >= "1" and s[i] <= "31":
            if not (s[i + 1] >= "0" and s[i + 1] <= "9"):
                if s[i + 2] >= "1000" and s[i + 2] <= "9999":
                    return (s[i], s[i + 1], s[i + 2])



#7

def maxstring(s):
    max = "0"
    countblank = 0
    for a in range(0, len(s)):
        if (s[a] == ' '):
            countblank += 1
    s = s.split(' ')
    for i in range(0, countblank):
        if s[i] > max and s[i].isnumeric():
            max = s[i]

    return max

#8
def minstring(s):
    min = float('inf')
    countblank = 0
    for a in range(0, len(s)):
        if (s[a] == ' '):
            countblank += 1
    s = s.split(' ')

    for i in range(0, countblank + 1):
        if s[i] < str(min) and s[i].isnumeric():
            min = s[i]
    return min

#9
def rownummax(s):
    max = 0
    arg = 1
    s = ''.join([s[i] for i in range(len(s)) if not (s[i] >= 'A' and s[i] <= 'z')])
    a = [0] * len(s)
    for j in range(1, len(s)):
        if int(s[j - 1]) + 1 == int(s[j]):
            arg = arg + 1
            a[j] = arg
        else:
            arg = 1

    max = '0'
    for i in range(0, len(s)):
        if a[i] > int(max):
            max = a[i]
    return int(max)


# zadane 9
def stringsort(s):
    print("введите строки")
    lst = []
    a = []
    for i in range(0, int(s)):
        print("№", i)
        lst.insert(i, input())
    for i in range(0, int(s)):
        a.append(len(lst[i]))
    a.sort()
    for i in range(0, int(s)):
        for j in range(0, int(s)):
            if a[i] == len(lst[j]):
                return (lst[j])


# задание 10
def srtringsortsekond(s):
    s = s.split(' ')
    s = sorted(s, key=len)
    return s





# задание 11
def countvowelsletter(word):
    count = 0
    word = word.lower()
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']:
            count += 1
    return count


def countconsonantletter(word):
    count = 0
    word = word.lower()
    for letter in word:
        if letter not in ['a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', '1', '2', '3',
                          '4', '5', '6', '7', '8', '9', '0']:
            count += 1
    return count


def sortbyletter(s):
    print("введите строки")
    lst = []
    count = 0
    a = []
    b = []
    for i in range(0, int(s)):
        print("№", i)
        lst.insert(i, input())
    for i in range(0, int(s)):
        a.append(countvowelsletter(lst[i]))
        b.append(countconsonantletter(lst[i]))
    b.sort()
    a.sort()
    print("по гласным")
    for i in range(0, int(s)):
        for j in range(0, int(s)):
            if a[i] == countvowelsletter(lst[j]):
                print(lst[j])
    print("по согласным")
    for i in range(0, int(s)):
        for j in range(0, int(s)):
            if b[i] == countconsonantletter(lst[j]):
                print(lst[j])


# 12
def ASCII(s):
    print("введите строки")
    lst = []
    a = []
    a2 = []
    x = 0
    for i in range(0, int(s)):
        print("№", i)
        lst.insert(i, input())
    for i in range(0, int(s)):
        x = 0
        for j in range(0, len(lst[i])):
            x += int(ord(lst[i][j]))
        x = x / len(lst[i])
        a.append(x)
    for i in range(0, len(a)):
        a2.append(((a[0] - a[i]) ** 2) ** 0.5)
    a2.sort()

    for i in range(0, int(s)):
        for j in range(0, int(s)):
            if a2[i] == ((a[0] - a[j]) ** 2) ** (1 / 2):
                print(lst[j])


# 13
def ASCII2(s):
    print("введите строки")
    lst = []
    a = []
    a2 = []
    x = 0
    for i in range(0, int(s)):
        print("№", i)
        lst.insert(i, input())
    for i in range(0, int(s)):
        x = 0
        for j in range(0, len(lst[i])):
            x += int(ord(lst[i][j]))
        x = x / len(lst[i])
        a.append(x)
    for i in range(0, len(a)):
        a2.append(((a[0] - a[i]) ** 2) ** 0.5)
    a2.sort()

    for i in range(0, int(s)):
        for j in range(0, int(s)):
            if a2[i] == ((a[0] - a[j]) ** 2) ** (1 / 2):
                print(lst[j])


# 14
def coollettercounter(s):
    print("введите строки")
    lst = []
    a=[]
    a2=[]
    lettercounterin = 0
    lettercounter=0
    allraws=''
    for i in range(0, int(s)):
        print("№", i)
        lst.insert(i, str(input()))
    for i in range(0, int(s)):
        allraws +=lst[i]
    allrawscount = sorted([(allraws.count(letter), letter) for letter in set(allraws)], reverse=True)
    for i in  range(0,len(allraws)):
        if allrawscount[0][1]==allraws[i]:
            lettercounter+=1
    for i in range(0, int(s)):
        lettercounterin = 0
        for j in range(0, len(lst[i])):
            if lst[i][j]==allrawscount[0][1]:
                lettercounterin+=1
        a.append(lettercounterin)
    for i in range(0, len(a)):
        a2.append(((lettercounter-a[i])**2)**0.5)
    a2.sort()
    for i in range(0, int(s)):
        for j in range(0, int(s)):
            if a2[i] == ((lettercounter-a[j])**2)**0.5:
                print(lst[j])


# 15
def pusharray(s):
    x = []
    for i in range(0, int(s)):
        x.append(int(input()))
    first = x[0]
    second = x[1]
    for i in range(0, int(s)):
        if (i < int(s) - 2):
            x[i] = x[i + 2]
    x[int(s) - 1] = second
    x[int(s) - 2] = first
    print(x)


# 16
def pusharray2(s):
    x = []
    for i in range(0, int(s)):
        x.append(int(input()))
    first = x[0]
    for i in range(0, int(s)):
        if (i < int(s) - 1):
            x[i] = x[i + 1]

    x[int(s) - 1] = first
    print(x)


# 17
def numcounter(s):
    x = []
    chetniy = 0
    for i in range(0, int(s)):
        x.append(int(input()))
    for i in range(0, int(s)):
        if x[i] % 2 == 0: chetniy += 1
    print(chetniy)


# 18
def mincounter(s):
    x = []
    counter = 0
    for i in range(0, int(s)):
        x.append(int(input()))
    for i in range(0, int(s)):
        if x[i] == min(x): counter += 1
    print(counter)


# 19
def sortcounter(s):
    x = []
    y = []
    numbercounter = [0] * int(s)
    rez = ''
    counter = 0
    for i in range(0, int(s)):
        x.append(int(input()))
    for i in range(0, int(s)):
        if (x[i] not in y):
            y.append(x[i])
    for i in range(0, len(y)):
        for j in range(0, len(x)):
            if y[i] == x[j]:
                numbercounter[i] += 1
    while sum(numbercounter) != 0:
        for i in range(0, len(y)):
            if numbercounter[i] == max(numbercounter):
                rez += str(y[i]) * numbercounter[i]
                numbercounter[i] = 0
    print(rez)

numoftusk=int(input("Введите номер задания"))
if numoftusk==1:
    mode=input("введите входное значение")
    print(first(mode))
if numoftusk==2:#кол-во нечетных чисел идущих до этого числа больше трех
    mode = input("введите входное значение")
    print(secondd(mode))
if numoftusk == 3:#произведение числа сумма цифор которого меньше самого числа например 14
    print(suminstr())
if numoftusk == 4:#кол-во русских
    mode = input("введите входное значение")
    print(countrus(mode))
if numoftusk == 5:#проверка на полиндром
    mode = input("введите входное значение")
    print(ispolindrom(mode))
if numoftusk == 6:#найти дату например рвлорылорваылоравол ловырловырлор лорывлоарлрывалорваы ловырдлардлывор 20 мая 2040 ловырлавоырлвыаорлвыа
    mode = input("введите входное значение")
    print(datafinder(mode))
if numoftusk == 7:#максимальное число например 999999999999 3298492 833 73
    mode = input("введите входное значение")
    print(maxstring(mode))
if numoftusk == 8:#мин число например 2 32987 233 782 0
    mode = input("введите входное значение")
    print(minstring(mode))
if numoftusk == 9:#наибольшее идущих под ряд
    mode = input("введите входное значение")
    print(rownummax(mode))
if numoftusk == 10:#сортировка по размеру
    mode = input("введите входное значение")
    print(srtringsortsekond(mode))
if numoftusk == 11:#сортировка по гласным и согласным на вход сначала количество
    mode = input("введите входное значение")
    print(sortbyletter(mode))
if numoftusk == 12:#в порядке увеличения квадратичного откланения на вход кол-во строк
    mode = input("введите входное значение")
    print(ASCII(mode))
if numoftusk == 13:#в порядке увеличения кв откланения частоты встречаемости популярного символа
    mode = input("введите входное значение")
    print(ASCII2(mode))
if numoftusk == 14:#В порядке увеличения кв отклонение частоты встречаемости самого частого символа сортировать строки
    mode = input("введите входное значение")
    print(coollettercounter(mode))
if numoftusk == 15:#Сдвиг массива вправо
    mode = input("введите входное значение")
    print(pusharray(mode))
if numoftusk == 16:#Сдвиг вправо на однгу позицию
    mode = input("введите входное значение")
    print(pusharray2(mode))
if numoftusk == 17:#количество четных эллемоентов в массиве
    mode = input("введите входное значение")
    print(numcounter(mode))
if numoftusk == 18:#кол-во минимальных эллементов в массиве
    mode = input("введите входное значение")
    print(mincounter(mode))
if numoftusk == 19:#сортировка строк по частоте встречаемости
    mode = input("введите входное значение")
    print(sortcounter(mode))
