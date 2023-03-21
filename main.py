f = open("passengers.txt", "r", encoding = 'utf-8')
n = f.readline()
n = int(n)
k = 0
max = 0
d = dict()
while True:
    line = f.readline()
    s = line.split()
    if not line:
        break
    a = [i for i in range(int(s[2]), int(s[3]) + 1)]
    d[s[0] + s[1]] = a


#переделать
for i in range(1, n + 1):
    for key in d.keys():
        if i in d.get(key):
            k+=1
        else:
            k-=1
        if k > max:
            max = k


print(max)
print(d)
f.close()
