# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyses the votes and calculates each of the following:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes ( = find all the uniuqe strings in a list)
# 3. The percentage of votes each candidate won.      (= votes for candidate/total number if votes cast)
# 4. The total number of votes each candidate won. 
# 5. The winner of the election based on popular vote.
from collections import OrderedDict
import operator
import os
import csv
from re import A
list_ID = []
list_country =[]
list_Candidate =[]
counter = 0
 
# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
# Percentage of votes won

 
with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     csv_header = next(csvreader)   
                                   #print (rows[1])  # print the second row
     

    #  rows = list(csvreader)
     for row in csvreader:
      list_ID.append(row[0])
      list_country.append(row[1])
      list_Candidate.append(row[2])
      

x = list_Candidate.count("Khan")
y = list_Candidate.count("Correy")
z= list_Candidate.count("Li")
a= list_Candidate.count("O'Tooley")
#percentages
percent_x= 100*x/len(list_ID)
percent_y= 100*y/len(list_ID)
percent_z= 100*z/len(list_ID)
percent_a= 100*a/len(list_ID)

# Dictionary with values of results so winner can be automated
Dict = {"Khan" : x, "O'Tooley": a, "Corry" : y, "Li" : z  }
new_ma_val = max(Dict.items(), key=operator.itemgetter(1))[0]
print(f"The winner is {new_ma_val}")     
 

unique_list = list(dict.fromkeys(list_Candidate))

#Simple version by checking the length and puttin in the Canidate results {unique_list[0]}:  {round(percent_x,3)}%     ({x}) manually for each candidate up to len(list_Candidate)
p = (f"Total Number of Votes Cast:{len(list_ID)}") 
q = (f"{unique_list[0]}:  {round(percent_x,3)}%     ({x})")
r= (f"{unique_list[1]}:  {round(percent_y,3)}%      ({y})")
s = (f"{unique_list[2]} :    {round(percent_z,3)}%     ({z})")
a2= (f"{unique_list[3]}:   {round(percent_a,3)}%     ({a})")

print("Election Results")
print("----------------------------------")
print (p)  
print("----------------------------------")
print(f"{q}  \n{r} \n{s} \n{a2}")
print("----------------------------------")
print(f"The winner is {new_ma_val}") 
print("----------------------------------")

f = open("PyPoll", "w")
f.write(f"Election Results\n---------------------------------- \n{p} \n{q} \n{r} \n{s} \n{a2} ")











