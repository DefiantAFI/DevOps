samplefile = open('routerlist.csv', 'r')

b = list()

for line in samplefile.readlines():
    a: list = list()
    line = line.strip('\n')
    a.insert(0, line)
    b.append(a)

print(b)
