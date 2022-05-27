# -----Code for the budget data ----
# #Create a Python script that analyses the records to calculate each of the following: 
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Notes on Calculations
# Average of the changes of P&L is two calculations  
# (difference between each cell) = changes and sum(changes)/range(columns)

# greatest increase/decreases are the maximum of the change in profit or loss and then find/show the relevant row of data


# Modules
from operator import index
import os
import csv

count_m = 0
row_count = 0 # count the number of row for the for loop to get the number of month/data points

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Lists to store data
month = []
pnl =[]
change =[]
count =0

list=[]
count = 0
total =0

total_diff =[]


# pnl1 = pnl[1]-pnl[0]
 #Open the CSV
 # define function above the with open??
with open(csvpath) as csvfile:
  
  csvreader = csv.reader(csvfile, delimiter=",")
  
  header =next(csvreader)
  for row in csvreader:
        
        
        # Add month
        month.append(row[0])
        # Make month list
        pnl.append(row[1])
        # make pnl list
        count = count +1
    
        total += int(row[1])    #int(row[1])   # total = total + int(row[1]) 
    
print("Financila Analysis")
print("--------------------------------")
print (f"Total Months:{len(month)}")
print(f"The total profit/loss:   {total}")












    
  


        
