import random
def funcount(a=[3],b=[5]):
    counter=0
    for i in  range(0,3):
        for j in range (0,5):
            if int(a[i])==int(b[j]):
                counter+=1
    return counter
n = int(input())
counter=0
randomnumber = []
answer=[]
randomnumber.append(random.randint(0,n-4))
for i in range(1, 3):
    randomnumber.append(randomnumber[i-1]+2)
randomnumber.sort()
for i in range(0, 5):
    answer.append(input("введите " + str(i) + "е чило"))
    if answer[i] == "HELP":
        print(randomnumber)
answer.sort()
if funcount(randomnumber,answer) == 3:
    print("YES")
else:
    print("NO")
flag = False
while flag == False :
    for i in range(0, 5):
        answer[i]=input("введите "+str(i)+"е чило   ")
        if answer[i]=="HELP":
            print(randomnumber)
            flag=True
            break
    if(flag==True):break
    answer.sort()
    if funcount(randomnumber, answer) == 3:
        print("YES")
    else: print("NO")
