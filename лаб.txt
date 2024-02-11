# 1
def first(n):
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
def second(n):
    rez = 0
    for i in range(1, n + 1):
        if i % 2 != 0 and i > 3:
            rez += 1
    return rez
#3
def trid(n):
    for i in range(1, n + 1):
        if n%i==0

n = int(input())
print(second(n))
#3
def suminstr():
    ch=int(input())
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
    print(rez,prov,chsum)
suminstr();

