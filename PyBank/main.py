# -----Code for the budget data ----
# #Create a Python script that analyses the records to calculate each of the following: 
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period


# First task is to read and open the csv file and skip that first line with the title

   # checked for the csv file to work print(f"Header:{csv_header}")

# total number of months: we just need to set up a count for the total number of 

# cells/data points in the month coloumn which is the range function

# Total profit/Loss is adding all the elements in the P&L column

# Average of the changes of P&L is two calculations  
# (difference between each cell) = changes and sum(changes)/range(columns)

# greatest increase/decreases are the maximum of the change in profit or loss and then find/show the relevant row of data
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Modules
from operator import index
import os
import csv
#import numpy as np ---- Does not work!
count_m = 0
row_count = 0 # count the number of row for the for loop to get the number of month/data points

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Lists to store data
month = []
pnl =[]
change =[]
count =0
pnl_total =0
list=[]
count = 0
total =0
 #Open the CSV
 # define function above the with open??
with open(csvpath) as csvfile:

  csvreader = csv.reader(csvfile, delimiter=",")
  
  header =next(csvreader)
  for row in csvreader:
        
        # count  = count + 1
        # print(header)
        # Add month
        month.append(row[0])
        count = count +1
        # add  pnl
        
        # del(pnl[0])
        # pnl.append(row[1])
        total += int(row[1])    #int(row[1])   # total = total + int(row[1]) 
print("Financila Analysis")
print("--------------------------------")
print(f"Total Months:     {count}" )
print(f"The total profit/loss:   {total}") 

        # for val in range(0, len(pnl)):
        #  total = total + pnl[val]
        
        








        


        # print("Financial Analysis ")
        # print("-------------------")
        # print (f"Total Months:{len(month)-1}") 
        # print(f"The total profit/loss: {pnlcount}")
    
    










    # for row in csvreader:
    #   #add up the total number of columns after the first row.
    #   count_m += int(row)    #int(row[1])   # total = total + int(row[1]) 
    #   total = int(row[1])
    #   totalpnl =(row[1])
    # print("Financial Analysis ")
    # print("-------------------")
    # print (f"Total Months:{len(rows)-1}") 
    # print(f"The total profit/loss: {totalpnl}")


      













    
   
    # for j in range(1,len(rows)):           # j from 1 to length-1
    #  k = j - 1                             # set the new k in the first outer loop
    #  row_list = []                         # reset row_list each time
     
    # for i in range (j, len(rows)):         # i from j to len-1
    #        change = (rows[i] - rows[k])    # get difference between each cell
    #        row_list.append(change)
    # print(row_list)                        # print out the distances for each outer loop iteration
   
  
    # split the pnl and month then add up the index 1 (P&L column) values
    
    #for line in rows:
      #   #Type = line.split(",")
      #   x = Type[1]
      #   y = Type[2]
        # print(rows)


        
