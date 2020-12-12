Python-Challenge
Ryan Brown
Created December 12, 2020

This repository contains two seperate analyses. The first is the PyBank analysis, and second is the PyPoll Analysis.

# PyBank Analysis

All of the scripts/resources for this analysis are found within the "PyBank" folder of the analyis. 
For this analysis, a csv file titled "budget_data" is used. This file is located within "PyBank"+"Resources".
This data contains two columns of data:

1. Date- which is the date the data is entered for.
2. Profit/losses- which is a dollar amount and can be positive or negative.

The budget_data csv contains 86 rows of data.

Using python language, the main.py file within the "PyBank folder" is used to analysize the data. 
The goal of this code is to do the calculate the following:
1. The total number of months included in the dataset
2. The net total amount of "Profit/Losses" over the entire period
3. Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
4. The greatest increase in profits (date and amount) over the entire period
5. The greatest decrease in losses (date and amount) over the entire period

These 5 goals are calculated within the main.py folder. The results are both printed to the terminal and to a text file.
The text file titled "output" is found within "PyBank"+"analysis".

# PyPoll Analysis

All of the scripts/resources for this analysis are found within the "PyPoll" folder of the analyis. 
For this analysis, a csv file titled "election_data" is used. This file is located within "PyPoll"+"Resources".
This data contains three columns of data:

1. Voter ID- the unique ID used for each voter.
2. County- the county in which the voter voted.
3. Candidate- the candidate that each voter voted for.

The election_data csv contains over one million rows of data.

Using python language, the main.py file within the "PyPoll" folder is used to analysize the data. 
The goal of this code is to do the calculate the following:
1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. The winner of the election based on popular vote.

These 5 goals are calculated within the main.py folder. The results are both printed to the terminal and to a text file.
The text file titled "output" is found within "PyPoll"+"analysis".



