import csv

samplefile = open('routerlist.csv', 'r')

# a = list()
# a = samplefile.read()

samplereader = csv.reader(samplefile)

print(samplereader, '\n')

newlistoflist = list(samplereader)

print(type(newlistoflist), '\n')
print(newlistoflist)

samplefile.close()
# print(a)
