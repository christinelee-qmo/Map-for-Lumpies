import csv

with open('../zipcodes/JP.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


    