numofcoun = int(input())
arrinfo = []
arrcoun=[""]*numofcoun
for i in range(0 , numofcoun):
    arrinfo.append(input())
for i in range(0 , numofcoun):
    for j in range(0,len(arrinfo[i])):
        arrcoun[i]+=arrinfo[i][j]
        if(arrcoun[i][j]==" "):break
numofcity=int(input())
arrcity=[""]*numofcity
for j in  range(0,numofcity):
    arrcity[j]=input()
for i in range(0,numofcoun):
    for j in  range(0,numofcity):
        if arrcity[j] in arrinfo[i]:arrcity[j]=arrcoun[i]
print(arrcity)
