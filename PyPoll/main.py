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
    candidate_list=set()
    khan_count=0
    correy_count=0
    li_count=0
    otooley_count=0


    # Loop through each of the csv file
    for row in csvreader:
        #Counting the number of votes
        count +=1
        #Creating list of candidates
        candidate_list.add(row[2])
        #Counting the number of votes for each candidate
        if row[2]=="Khan":
            khan_count+=1
        elif row[2]=="Correy":
            correy_count+=1
        elif row[2]=="Li":
            li_count+=1
        elif row[2]=="O'Tooley":
            otooley_count+=1
        #Calculating the percentage of votes for each candidate
        khan_percent=round((khan_count/count)*100,4)
        correy_percent=round((correy_count/count)*100,4)
        otooley_percent=round((otooley_count/count)*100,4)
        li_percent=round((li_count/count)*100,4)
        #Formatting results to be to 3 decimal places
        khan="{:.3f}".format(khan_percent)
        correy="{:.3f}".format(correy_percent)
        otooley="{:.3f}".format(otooley_percent)
        li="{:.3f}".format(li_percent)
        #Calculating the winner
        winner_list = [khan, correy, otooley, li]
        winner = max(winner_list)
        #Changing format of winner's name
        if winner == khan:
            winner ="Khan"
        elif winner == correy:
            winner = "Correy"
        elif winner == otooley:
            winner = "O'tooley"
        elif winner == li:
            winner = "li"

            

        

    #Print out the results
    print("Election Results")
    print("---------------------------------")
    print(f"Total Votes: {count}")
    print("---------------------------------")
    print(f"Khan: {khan}% ({khan_count})")
    print(f"Correy: {correy}% ({correy_count})")
    print(f"Li: {li}% ({li_count})")
    print(f"O'Tooley: {otooley}% ({otooley_count})")
    print("---------------------------------")
    print(f'Winner: {winner}')
    print("---------------------------------")

# Specify the file to write to
output_path = os.path.join("analysis", "output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:


    # Write the first row (column headers)
    txtfile.write(f"Election Results\r\n---------------------------------\r\nTotal Votes: {count}\r\n---------------------------------\r\nKhan: {khan}% ({khan_count})\r\nCorrey: {correy}% ({correy_count})\r\nLi: {li}% ({li_count})\r\nO'Tooley: {otooley}% ({otooley_count})\r\n---------------------------------\r\nWinner: {winner}\r\n---------------------------------")
