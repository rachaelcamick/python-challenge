# Dependencies
import os
import csv
# path to collect data from budget file
csvpath = os.path.join("budget_data.csv")
# make empty lists
months = []
net_profit =[]
monthly_change = []
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header so list includes only values
    skipheader = next(csvreader)
    # loop through rows in the data file
    for row in csvreader: 
        months.append(row[0])
        net_profit.append(int(row[1]))
    # loop through the length of the list
    for i in range(1, len(net_profit)-1):
        #make a list comprised of the profit changes between months
        monthly_change.append((int(net_profit[i+1]) - int(net_profit[i])))
#find monthly max and min
increase_max = max(monthly_change)
decrease_max = min(monthly_change)
#find greatest increase and decrease in profits 
increase_month = monthly_change.index(max(monthly_change))
decrease_month = monthly_change.index(min(monthly_change))
# print statements
print("Financial Analysis")
print(f"Total Months: {len(months)}")
print(f"Net Profit/Losses: ${sum(net_profit)}")
print(f"Average Change: ${sum(monthly_change)/len(monthly_change)}")
print(f"Greatest Increase in Profits: {months[increase_month]} ${[increase_max]}")
print(f"Greatest Decrease in Profits: {months[decrease_month]} ${[decrease_max]}")
