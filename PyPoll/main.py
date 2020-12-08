###### PyPoll Analysis Main ######
######      Ryan Brown      ######
######  December 8, 2020    ######

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