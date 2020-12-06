###### PyBank Analysis Main ######
######      Ryan Brown      ######
######  December 6, 2020    ######

# Loading tools to import csv
import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources','budget_data.csv')

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    print((csvreader))
    header = next(csvreader)

    print("Financial Analysis")
    print("---------------------------------")

    # Setting each of the variables to be used in the loop below
    count = 0
    net_profit = 0
    profit_change = 0

    # Loop through each of the csv file
    for row in csvreader:
        #Counting the number of months
        count +=1
        #Adding names to the variables
        date = str(row[0])
        profit_loss = int(row[1])
        #Calculating the net profit/loss
        net_profit += profit_loss
        #Calculating the changes in profit/loss
        profit_change = 
    #Print out the results
    print(f"Total Months: {count}")
    print(f"Total: ${net_profit}")

    


