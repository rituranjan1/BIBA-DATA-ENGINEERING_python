import csv
with open("names.csv", 'r') as file:
    csvreader = csv.reader(file)
    
    for line in csvreader:
        print(line)