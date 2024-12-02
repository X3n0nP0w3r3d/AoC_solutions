def count_time(p, q, l, r, a, b, c, d):
    ans = 0
    for i in range(l, r + 1):
        flag = False
        for j in range(p):
            if i >= a[j] and i <= b[j]:
                flag = True
                break
        if not flag:
            continue
        for j in range(q):
            if i - c[j] >= 0 and i - d[j] <= 0:
                ans += 1
                break
    return ans


p, q, l, r = map(int, input().split())
a = []
b = []
for i in range(p):
    aa, bb = map(int, input().split())
    a.append(aa)
    b.append(bb)
c = []
d = []
for i in range(q):
    cc, dd = map(int, input().split())
    c.append(cc)
    d.append(dd)
print(count_time(p, q, l, r, a, b, c, d))



