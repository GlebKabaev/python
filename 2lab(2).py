dict = {}
ar=[]

cin = int(input("Введите количество стран: "))
for i in range(cin):
    string = str(input("Введите страну и города: ")).split(" ")
    country = string.pop(0)
    dict.update({country: string})

cin = int(input("Введите количество городов: "))
for i in range(cin):
    city = str(input("Введите город: "))
    for key in list(dict.keys()):
        if city in dict[key]:
            ar.append(key)
print(ar)
