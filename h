[33mcommit 1d5f370d15b1c218aedd48ad806a88f190c24a93[m[33m ([m[1;36mHEAD -> [m[1;32mmain[m[33m)[m
Author: Rob397 <105466612+Rob397@users.noreply.github.com>
Date:   Thu May 26 16:24:28 2022 +1000

    PyBank improvement
    
    Now the Months and Total both print at the same time!

[1mdiff --git a/PyBank/main.py b/PyBank/main.py[m
[1mindex 7d3d31f..b1772c4 100644[m
[1m--- a/PyBank/main.py[m
[1m+++ b/PyBank/main.py[m
[36m@@ -28,41 +28,111 @@[m [mfrom operator import index[m
 import os[m
 import csv[m
 #import numpy as np ---- Does not work![m
[31m-total = 0[m
[32m+[m[32mcount_m = 0[m
 row_count = 0 # count the number of row for the for loop to get the number of month/data points[m
 [m
[31m-change = 0[m
[31m-[m
 # Set path for file[m
 csvpath = os.path.join("Resources", "budget_data.csv")[m
 [m
[32m+[m[32m# Lists to store data[m
[32m+[m[32mmonth = [][m
[32m+[m[32mpnl =[][m
[32m+[m[32mchange =[][m
[32m+[m[32mcount =0[m
[32m+[m[32mpnl_total =0[m
[32m+[m[32mlist=[][m
[32m+[m[32mcount = 0[m
[32m+[m[32mtotal =0[m
  #Open the CSV[m
  # define function above the with open??[m
 with open(csvpath) as csvfile:[m
[31m-    [m
[31m-    csvreader = csv.reader(csvfile)[m
[31m-    #csv_header = next(csvreader)   #an put print(csv_header) to check it worked[m
[31m-   #print (rows[1])  # print the second row[m
[32m+[m
[32m+[m[32m  csvreader = csv.reader(csvfile, delimiter=",")[m
   [m
[31m-    rows = list(csvreader)[m
[32m+[m[32m  header =next(csvreader)[m
[32m+[m[32m  for row in csvreader:[m
[32m+[m[41m        [m
[32m+[m[32m        # count  = count + 1[m
[32m+[m[32m        # print(header)[m
[32m+[m[32m        # Add month[m
[32m+[m[32m        month.append(row[0])[m
[32m+[m[32m        count = count +1[m
[32m+[m[32m        # add  pnl[m
[32m+[m[41m        [m
[32m+[m[32m        # del(pnl[0])[m
[32m+[m[32m        # pnl.append(row[1])[m
[32m+[m[32m        total += int(row[1])    #int(row[1])   # total = total + int(row[1])[m[41m [m
[32m+[m[32mprint("Financila Analysis")[m
[32m+[m[32mprint("--------------------------------")[m
[32m+[m[32mprint(f"Total Months:     {count}" )[m
[32m+[m[32mprint(f"The total profit/loss:   {total}")[m[41m [m
 [m
[31m-    #add up the total number of columns after the first row.[m
[31m-    print (f"Total Months:{len(rows)-1}")      [m
[31m-    for row in csvreader:[m
[31m-   [m
[31m-      total += int(row[1])    #int(row[1])   # total = total + int(row[1]) [m
[32m+[m[32m        # for val in range(0, len(pnl)):[m
[32m+[m[32m        #  total = total + pnl[val][m
[32m+[m[41m        [m
[32m+[m[41m        [m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m[41m        [m
[32m+[m
[32m+[m
[32m+[m[32m        # print("Financial Analysis ")[m
[32m+[m[32m        # print("-------------------")[m
[32m+[m[32m        # print (f"Total Months:{len(month)-1}")[m[41m [m
[32m+[m[32m        # print(f"The total profit/loss: {pnlcount}")[m
[32m+[m[41m    [m
     [m
[31m-    print(f"The total profit/loss:   {total}")[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m[32m    # for row in csvreader:[m
[32m+[m[32m    #   #add up the total number of columns after the first row.[m
[32m+[m[32m    #   count_m += int(row)    #int(row[1])   # total = total + int(row[1])[m[41m [m
[32m+[m[32m    #   total = int(row[1])[m
[32m+[m[32m    #   totalpnl =(row[1])[m
[32m+[m[32m    # print("Financial Analysis ")[m
[32m+[m[32m    # print("-------------------")[m
[32m+[m[32m    # print (f"Total Months:{len(rows)-1}")[m[41m [m
[32m+[m[32m    # print(f"The total profit/loss: {totalpnl}")[m
[32m+[m
[32m+[m
[32m+[m[41m      [m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
     [m
    [m
[31m-    for j in range(1,len(rows)):           # j from 1 to length-1[m
[31m-     k = j - 1                    # set the new k in the first outer loop[m
[31m-     row_list = []                # reset row_list each time[m
[32m+[m[32m    # for j in range(1,len(rows)):           # j from 1 to length-1[m
[32m+[m[32m    #  k = j - 1                             # set the new k in the first outer loop[m
[32m+[m[32m    #  row_list = []                         # reset row_list each time[m
      [m
[31m-    for i in range (j, len(rows)):          # i from j to len-1[m
[31m-           change = (rows[i] - rows[k])              # get difference between each cell[m
[31m-           row_list.append(change)[m
[31m-    print(row_list)                         # print out the distances for each outer loop iteration[m
[32m+[m[32m    # for i in range (j, len(rows)):         # i from j to len-1[m
[32m+[m[32m    #        change = (rows[i] - rows[k])    # get difference between each cell[m
[32m+[m[32m    #        row_list.append(change)[m
[32m+[m[32m    # print(row_list)                        # print out the distances for each outer loop iteration[m
    [m
   [m
     # split the pnl and month then add up the index 1 (P&L column) values[m
[1mdiff --git a/PyPoll/main.py b/PyPoll/main.py[m
[1mindex 3215f36..e2a9843 100644[m
[1m--- a/PyPoll/main.py[m
[1m+++ b/PyPoll/main.py[m
[36m@@ -25,6 +25,8 @@[m [mwith open(csvpath) as csvfile:[m
      print("Election Results")[m
      print("----------------------------------")[m
      print (f"Total Number of Votes Cast:{len(rows)-1}")      [m
[41m+     [m
[41m+  [m
     [m
 [m
 [m
