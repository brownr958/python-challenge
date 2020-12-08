###### PyPoll Analysis Main ######
######      Ryan Brown      ######
######  December 8, 2020    ######

# Loading tools to import csv
import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources','election_data.csv')

# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    print((csvreader))
    header = next(csvreader)
    # Setting each of the variables to be used in the loop below
    count = 0


    # Loop through each of the csv file
    for row in csvreader:
        #Counting the number of votes
        count +=1

    #Print out the results
    print("Election Results")
    print("---------------------------------")
    print(f"Total Votes: {count}")
    print("---------------------------------")

        