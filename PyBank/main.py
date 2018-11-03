# Dependencies
import os
import csv
# path to collect data from budget file
csvpath = os.path.join("budget_data")
# make empty lists
months = []
net_profit =[]
monthly_change = []
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
    for i in list(len(net_profit)):
        #make a list comprised of the profit changes between months
        monthly_change.append(net_profit(i+1)-net_profit(i))
# find monthly max and min
increase_max = max(monthly_change)
decrease_max = min(monthly_change)
# identify the month based on the index
increase_month = monthly_change.index(max(monthly_change))
decrease_month = monthly_change.index(min(monthly_change))


