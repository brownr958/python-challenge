###### PyPoll Analysis Main ######
######      Ryan Brown      ######
######  December 8, 2020    ######

# Loading tools to import csv
import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources','election_data.csv')

    # Setting each of the variables to be used in the loop below
count = 0
candidate_list= []
candidates = {}

# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Setting the first row to be the column names
    header = next(csvreader)


    # Loop through each of the csv file
    for row in csvreader:
        #Counting the number of votes
        count +=1
        #Setting candidate name variable to correct value
        candidate_name = row[2]
        #Adding candidate names to a unique list 
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            #Setting the count variable that will count individual's votes
            candidates[candidate_name] =0
        #Telling the votes to be counted each time the candidate name appears
        candidates[candidate_name] = candidates[candidate_name] + 1 

# Beginning the Output file in order to write the print statements to the text file. 
# Loops are used and therefore must be within the output writting "with" in order to then write them to the text file without loosing the information.
# Specify the file to write to
output_path = os.path.join("analysis", "output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    #Printing the title of my analysis and the total vote count
    print("Election Results")
    print("---------------------------------")
    print(f"Total Votes: {count}")
    print("---------------------------------")
    #Writting the prints aboce to the text file
    txtfile.write(f'Election Results\r\n---------------------------------\r\nTotal Votes: {count}\r\n---------------------------------\r\n')

    #Setting for loop to run through each name
    for candidate in candidates:
        #Collecting the number of votes per candidate
        votes = candidates.get(candidate)
        #Calculating the percentage of their votes 
        vote_percentage = float(votes) / float(count) * 100
        #Editing the format of the percentage to have 3 decimal places
        vote_percentage_format="{:.3f}".format(vote_percentage)
        #Printing the results of the analysis
        print(f'{candidate}: {vote_percentage_format}% ({votes})')
        #Writting the prints above to the textfile
        txtfile.write(f'{candidate}: {vote_percentage_format}% ({votes})\r\n')
    #Obtaining the winner of the election
    winner = max(candidates,key=candidates.get)
    #Printing the winner results
    print("---------------------------------")
    print(f'Winner: {winner}')
    print("---------------------------------")
    #Writting the prints above to the textfile
    txtfile.write(f'---------------------------------\r\nWinner: {winner}\r\n---------------------------------')

