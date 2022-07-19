#Your task is to create a Python script that analyzes the records to calculate each of the following values:

from itertools import count
import os
import csv
import sys

os.chdir(sys.path[0])
csvpath = os.path.join('Resources', 'budget_data.csv')

months = []
profits = []
profitchange = []
headers = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    # Read and store headers
    headers = next(csvreader)

    # Read and store each row in profits and months lists
    for row in csvreader:
        months.append(row[0])
        
        profit_num = int(row[1])
        profits.append(profit_num)

# Open analysis file to write to and create if does not exist
analysis_path = os.path.join('analysis', 'pybank_analysis.txt')
with open(analysis_path, 'w') as analysis_file:
    analysis_file.write("Financial Analysis \n")
    print("Financial Analysis")

    analysis_file.write("--------------- \n")
    print("---------------")

    #The total number of months included in the dataset
    analysis_file.write(f"Total Months: {len(months)} \n")
    print(f"Total Months: {len(months)}")

    #The net total amount of "Profit/Losses" over the entire period
    analysis_file.write(f"Total: ${sum(profits)} \n")
    print(f"Total: ${sum(profits)}")

    #List of the changes in "Profit/Losses" over the entire period
    for i in range(len(profits)-1):
        current_profit = int(profits[i])
        next_profit = int(profits[i+1])
        profitchange.append(next_profit - current_profit)

    #The average profit change
    profit_change_average = sum(profitchange) / len(profitchange)
    analysis_file.write(f"Average Change: ${profit_change_average} \n")
    print(f"Average Change: ${profit_change_average}")

    #The greatest increase in profits (date and amount) over the entire period
    max_profit_change = max(profitchange)
    profit_change_index = profitchange.index(max_profit_change)
    max_change_month = months[profit_change_index + 1]

    analysis_file.write(f"Greatest Increase in Profits: {max_change_month} (${max_profit_change}) \n")
    print(f"Greatest Increase in Profits: {max_change_month} (${max_profit_change})")

    #The greatest decrease in profits (date and amount) over the entire period
    min_profit_change = min(profitchange)
    min_change_month = months[profitchange.index(min_profit_change) + 1]

    analysis_file.write(f"Greatest Decrease in Profits: {min_change_month} (${min_profit_change}) \n")
    print(f"Greatest Decrease in Profits: {min_change_month} (${min_profit_change})")



