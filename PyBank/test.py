import csv
with open("budget_data.csv", "r") as file:
    filereader = csv.reader(file)
    for row in filereader:
        print(row[0])