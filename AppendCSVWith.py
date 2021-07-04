import csv

print("Please add a new router to the list")
hostname = input("What is the hostname? ")
ip = input("What is the ip address? ")
location = input("What is the location? ")

router = [hostname, ip, location]

with open("routerlist.csv", "a") as data:
    csv_writer = csv.writer(data)
    csv_writer.writerow(router)

# with open('routerlist.csv', 'r') as data:
    # rlreader = csv.reader(data)
    # rllist = list(data)
    # rlstring = data.read()
    # print(rllist)
    # print(rlstring)

# print(f' \n Hope the following prints the routerlist file: /n{rlstring}')
input('Hello: ')
