# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyses the votes and calculates each of the following:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

import os
import csv


# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

 #Open the CSV
 # define function above the with open??
with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
      #csv_header = next(csvreader)   #an put print(csv_header) to check it worked
       #print (rows[1])  # print the second row
  
     rows = list(csvreader)
     
     print("Election Results")
     print("----------------------------------")
     print (f"Total Number of Votes Cast:{len(rows)-1}")      
    


