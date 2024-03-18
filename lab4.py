f = open('C:/Users/glebk/Desktop/27-124a.txt')
n, k, v, m = map(int, f.readline().split())
a = [0] * k
for _ in range(n):
    z, p = map(int, f.readline().split())
    a[z % k] = p // v + (p % v > 0)
cm = sum(a)
if m < k // 2:
    c = sum(a[:m * 2 + 1])
    cm = c if a[m] else 0
for i in range(1, k):
    c += a[(i + m * 2) % k] - a[i - 1]
    if a[(i + m) % k]:
        cm = max(cm, c)
for s in ['C:/Users/glebk/Desktop/27-124a.txt', 'C:/Users/glebk/Desktop/27-124b.txt']:
    f = open(s)
    n, k, v, m = map(int, f.readline().split())
    a = [0] * k
    for _ in range(n):
        z, p = map(int, f.readline().split())
        a[z % k] = p // v + (p % v > 0)
    cm = sum(a)
    if m < k // 2:
        c = sum(a[:m * 2 + 1])
        cm = c if a[m] else 0
        for i in range(1, k):
            c += a[(i + m * 2) % k] - a[i - 1]
            if a[(i + m) % k]:
                cm = max(cm, c)
    print(cm)
