import csv

samplefile = open('routerlist.csv')
samplereader = csv.reader(samplefile)
sampledata = list(samplereader)
print(sampledata)
print(type(sampledata))
