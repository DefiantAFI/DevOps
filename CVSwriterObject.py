import csv

print("Please add a new router to the list")
hostname = input("What is the hostname? ")
ip = input("What is the ip address? ")
location = input("What is the location? ")


router = [hostname, ip, location]

with open("routerlistwriter.csv", "a") as data:
    csv_writer = csv.writer(data)
    csv_writer.writerow(router)
