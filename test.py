x = {}
n = int(input('nhap so hoc sinh: '))
for _ in range(n):
    name = input()
    score = float(input())
    x[name] = score
value = list(set(x.values()))
value.sort()
name = []
for k,v in x.items():
    if v == value[1]:
        name.append(k)
name.sort()
for i in (name):
     print(name)