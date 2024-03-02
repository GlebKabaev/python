import random
randomnumber = set([])
answer = set([])
n = int(input())
flag=False
while flag==False:
    answer.clear()
    while (len(randomnumber))!=3:
        randomnumber.add(random.randint(1,n))
    for i in range(0, 5):
        answerin=input()
        if answerin!="HELP":
            answer.add(int(answerin))
        else:
            print(randomnumber)
            flag=True
            break
    if(flag==True):break
    startcount = len(answer)
    answer=answer-randomnumber
    nowcount = len(answer)
    if nowcount==2:
        print("YES")
    else:print("NO")

