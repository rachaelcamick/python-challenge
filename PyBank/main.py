# Dependencies
import os
import csv
# path to collect data from budget file
csvpath = os.path.join("budget_data")
# make empty lists
months = []
net_profit =[]
monthly_profit = []
#open file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header so list includes only values
    skipheader = next(csvreader)
    # now loop through rows
    for row in csvreader: 
        months.append(row[0])
        net_profit.append(row[1])
        





