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

    # Setting each of the variables to be used in the loop below
    count = 0
    net_profit = 0
    profit_change = 0
    #Setting Previous Profit as the Value in Jan-10
    prev_profit = 867884
    ave_profit = 0
    total_change = 0
    #Setting value for previous profit change
    prev_change = 0
    prev_change2 = 0

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
        profit_change=(profit_loss - prev_profit)
        #Replacing Previous Profit change if it is less than
        if prev_change2 >= profit_change:
            prev_change2 = prev_change2
        else: 
            prev_change2 = profit_change
            prev_change2_date = str(row[0])
        #Replacing Previous Profit change if it is less than
        if prev_change <= profit_change:
            prev_change = prev_change
        else: 
            prev_change = profit_change
            prev_change_date = str(row[0])
        #Replacing previous profit value
        prev_profit = int(row[1])
        #Calculating the average of the changes
        total_change +=profit_change
        ave_profit=round((total_change/85),2)
        


    #Print out the results
    print("Financial Analysis")
    print("---------------------------------")
    print(f"Total Months: {count}")
    print(f"Total: ${net_profit}")
    print(f"Average Change: ${ave_profit}")
    print(f"Greatest Increase in Profits: {prev_change2_date} (${prev_change2})")
    print(f"Greatest Decrease in Profits: {prev_change_date} (${prev_change})")

# Specify the file to write to
output_path = os.path.join("analysis", "output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:


    # Write the first row (column headers)
    txtfile.write(f"Financial Analysis \r\n--------------------------------- \r\nTotal Months: {count}\r\nTotal: ${net_profit}\r\nAverage Change: ${ave_profit}\r\nGreatest Increase in Profits: {prev_change2_date} (${prev_change2})\r\nGreatest Decrease in Profits: {prev_change_date} (${prev_change})")



    


