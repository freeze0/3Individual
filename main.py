f = open("passengers.txt", "r", encoding = 'utf-8')
n = f.readline()
n = int(n)
k = 0
max = 0
d = dict()
peresadki = dict()

while True:
    line = f.readline()
    s = line.split()
    if not line:
        break
    a = [i for i in range(int(s[2]), int(s[3]) + 1)]
    d[s[0] + s[1]] = a

for i in range(1, n):
    pass_count = 0
    for value in d.values():
        if i in value and i != value[len(value) - 1]:
            pass_count += 1
    if max < pass_count:
        max = pass_count
    peresadki[str(i) + '-' + str(i+1)] = pass_count

print(d)
print(peresadki)
for key, value in peresadki.items():
    if value == max:
        print(key)
f.close()
