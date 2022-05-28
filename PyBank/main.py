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
from re import A
from typing import Counter

count_m = 0
row_count = 0 # count the number of row for the for loop to get the number of month/data points

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Lists to store data
month = []
pnl =[]
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


a = (f"Total Months:{len(month)}")
b = (f"The total profit/loss:   {total}")


# -----------below in comment lines is my approach for change in price and the max/min values------
# set_1  =[]
# set_2 = []
# change = set_2 - set_1
# for i in pnl:
  
#   set_1.append(int(pnl[i]))
#   set_2.append(int(pnl[i+1]))
# max_change = max(change)
# min_change =min(change)

# # Greatest Increase in Profits: Feb-2012 ($1926159)
# # Greatest Decrease in Profits: Sep-2013 ($-2196167)
# c=  (f"Greatest Increase in Profits:  {max_change}")
# d = (f"Greatest Decrease in Profits: {min_change}")

print("Financila Analysis")
print("--------------------------------")

print (a)
print(b)
# print(f"Average  Change:   {change}")
# print(c)
# print(d)


f = open("PyBank", "w")
f.write(f"Financila Analysis\n--------------------------------\n{a} \n{b}")



  














    
  


        
