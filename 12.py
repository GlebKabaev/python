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
    for i in range(0, len(lst[i])):
        a2.append(((a[0]-a[i])**2)**(1/2))
    a2.sort()
    #############################################
    for i in range(0, int(s)):
        for j in range(0, int(s)):
            if a[i] == countvowelsletter(lst[j]):
                print(lst[j])




x = input()
print(ASCII(x))
