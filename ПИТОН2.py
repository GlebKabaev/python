import string
import math
def countrus(s):
    count = 0
    for i in range(0,len(s)):
        if s[i]>='А' and s[i]<='я':
            count+=1
    return count
def ispolindrom(s):
    flag=True

    for i in  range(0,len(s)//2):
        if(s[i]!=s[len(s)-i-1]):
            flag=False
    return flag
def datafinder(s):
    countblank=0
    for a in range (0,len(s)):
        if(s[a]==' '):
            countblank +=1
    s=s.split(' ')
    for i in  range(0,countblank):
        if s[i]>="1" and s[i]<="31":
            if not(s[i+1]>="0"and s[i+1]<"9"):
                if s[i+2]>="1000" and s[i+2]<="9999":
                    print (s[i],s[i+1],s[i+2])





from fractions import Fraction
def maxstring(s):
    max="0"
    countblank = 0
    for a in range(0, len(s)):
        if (s[a] == ' '):
            countblank += 1
    s = s.split(' ')
    for i in range(0, countblank):
        if s[i]>max and s[i].isnumeric():
            max=s[i]

    return max
def minstring(s):
    min = float('inf')
    countblank = 0
    for a in range(0, len(s)):
        if (s[a] == ' '):
            countblank += 1
    s = s.split(' ')

    for i in range(0, countblank+1):
        if s[i] < str(min) and s[i].isnumeric():
            min = s[i]
    return min
def rownummax(s):
    max=0
    arg=1
    s = ''.join([s[i] for i in range(len(s)) if not(s[i]>='A' and s[i]<='z')])
    a=[0]*len(s)
    for j in range(1, len(s)):
        if  int(s[j - 1]) + 1 == int(s[j]):
            arg=arg+1
            a[j]=arg
        else:
            arg=1

    max = '0'
    for i in range(0,len(s)):
        if a[i]>int(max):
            max=a[i]
    return int(max)




#zadane 9
def stringsort(s):
    print("введите строки")
    lst=[]
    a=[]
    for i in  range (0,int(s)):
        print("№",i)
        lst.insert(i,input())
    for i in range(0,int (s)):
        a.append(len(lst[i]))
    a.sort()
    for i in range(0,int(s)):
        for j in range(0,int(s)):
            if a[i]==len(lst[j]):
                print(lst[j])
#задание 10
def srtringsortsekond(s):
    s = s.split(' ')
    s=sorted(s,key=len)
    return s
s=(input())
stringsort(s)

#задание 11
def countvowelsletter(word):
    count=0
    word = word.lower()
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я','1','2','3','4','5','6','7','8','9','0']:
            count += 1
    return count

def countconsonantletter(word):
    count = 0
    word = word.lower()
    for letter in word:
            if letter not in ['a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я','1','2','3','4','5','6','7','8','9','0']:
                count += 1
    return count

def sortbyletter(s):
    print("введите строки")
    lst = []
    count=0
    a = []
    b = []
    for i in range(0, int(s)):
        print("№", i)
        lst.insert(i, input())
    for i in  range(0,int(s)):
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
#12
def ASCII(s):
    print("введите строки")
    lst = []
    a=[]
    a2=[]
    x = 0
    for i in range(0, int(s)):
        print("№", i)
        lst.insert(i, input())
    for i in range(0, int(s)):
        x=0
        for j in range(0, len(lst[i])):
            x += int(ord(lst[i][j]))
        x=x/len(lst[i])
        a.append(x)
    for i in range(0, len(a)):
        a2.append(((a[0]-a[i])**2)**0.5)
    a2.sort()
    
    for i in range(0, int(s)):
        for j in range(0, int(s)):
            if a2[i] == ((a[0]-a[j])**2)**(1/2):
                print(lst[j])
#13
def ASCII2(s):
    print("введите строки")
    lst = []
    a=[]
    a2=[]
    x = 0
    for i in range(0, int(s)):
        print("№", i)
        lst.insert(i, input())
    for i in range(0, int(s)):
        x=0
        for j in range(0, len(lst[i])):
            x += int(ord(lst[i][j]))
        x=x/len(lst[i])
        a.append(x)
    for i in range(0, len(a)):
        a2.append(((a[0]-a[i])**2)**0.5)
    a2.sort()

    for i in range(0, int(s)):
        for j in range(0, int(s)):
            if a2[i] == ((a[0]-a[j])**2)**(1/2):
                print(lst[j])
#14
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
        lst.insert(i, input())
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
#15
def pusharray(s):
    x=[]
    for i in range(0,int(s)):
        x.append(int(input()))
    first=x[0]
    second=x[1]
    for i in range(0,int(s)):
        if(i<int(s)-2):
            x[i]=x[i+2]
    x[int(s)-1]=second
    x[int(s)-2]=first
    print(x)
#16
def pusharray2(s):
    x=[]
    for i in range(0,int(s)):
        x.append(int(input()))
    first=x[0]
    for i in range(0,int(s)):
        if(i<int(s)-1):
            x[i]=x[i+1]

    x[int(s)-1]=first
    print(x)
#17
def numcounter(s):
    x=[]
    chetniy = 0
    for i in range(0,int(s)):
        x.append(int(input()))
    for i in range(0, int(s)):
        if x[i]%2==0:chetniy+=1
    print(chetniy)
#18
def mincounter(s):
    x=[]
    counter = 0
    for i in range(0,int(s)):
        x.append(int(input()))
    for i in range(0, int(s)):
        if x[i]==min(x):counter+=1
    print(counter)
#19
def sortcounter(s):
    x=[]
    y=[]
    numbercounter=[0]*int(s)
    rez=''
    counter = 0
    for i in range(0,int(s)):
        x.append(int(input()))
    for i in range(0, int(s)):
        if(x[i] not in y):
            y.append(x[i])
    for i in range(0, len(y)):
        for j in range(0, len(x)):
            if y[i]==x[j]:
                numbercounter[i]+=1
    while sum(numbercounter)!=0:
        for i in range(0, len(y)):
            if numbercounter[i]==max(numbercounter):
                rez += str(y[i]) * numbercounter[i]
                numbercounter[i]=0
    print (rez)









