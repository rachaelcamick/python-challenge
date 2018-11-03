# Dependencies
import os
import csv
# path to collect data from budget file
csvpath = os.path.join("budget_data")
# make empty lists
months = []
net_profit =[]
monthly_profit_delta = []
#open file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header so list includes only values
    skipheader = next(csvreader)
    # loop through rows in the data file
    for row in csvreader: 
        months.append(row[0])
        net_profit.append(row[1])
    # loop through the length of the list
    for i in range(len(net_profit)):
        monthly_profit_delta.append(net_profit(i+1)-net_profit(i))
    
