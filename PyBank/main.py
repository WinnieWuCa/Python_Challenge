#Pybank

import os
import csv

file_path = os.path.join("budget_data.csv")
with open(file_path,newline="")as csv_file:
    file_holder = csv.reader(csv_file, delimiter =",")
    next(file_holder)
    i = 1
    month =""
    counter_month = 0
    counter_total = 0
    last_pl = 0
    delta_pl = 0
    counter_delta=0 
    greatest_month_inc = "" 
    greatest_month_dec = "" 
    greatest_inc = 0
    greatest_dec =0
    j = 0
   
   # -------------------------------------------------------------------
   #Loop through the files & calculate the info
   #  - The total number of months included in the dataset 
   #  - The net total amount of "Profit/Losses" over the entire period
   #  - The average of the changes in "Profit/Losses" over the entire period
   #  - The greatest increase in profits (date and amount) over the entire period
   #  - The greatest decrease in losses (date and amount) over the entire period
   # -------------------------------------------------------------------
    for row in file_holder:

        counter_total = counter_total + int(row[1])
        
        if row[0] != month:
            counter_month = counter_month +1
            month = row[0] 

        delta_pl = int(row[1])-last_pl  
        
        if i == 1:
            i = i+1
        else:
            counter_delta = counter_delta + delta_pl
         
        if delta_pl > greatest_inc:
            greatest_month_inc  = row[0]
            greatest_inc = delta_pl
             
        if delta_pl < greatest_dec:
            greatest_month_dec = row[0]
            greatest_dec = delta_pl
        
        last_pl = int(row [1])
    
    avg_change = (counter_delta /(counter_month-1)) 
    avg_change = round(avg_change,2)

        # Multipel lists to keep the info
    greatinc =str(greatest_month_inc) + " " + str(greatest_inc)
    greatdec =str(greatest_month_dec) + " " + str(greatest_dec)
    numbers = ["Total Months: ", "Total: ", "Average Change: ", "Greatest Increase in Profits: ", "Greatest Decrease in Profits: " ]
    greatest = [counter_month,counter_total, avg_change,greatinc, greatdec]
    
    # -------------------------------------------------------------------
    # Write to a newly created output file
    # -------------------------------------------------------------------
    output = zip(numbers, greatest)
    output_file = os.path.join("output_file.csv")
    with open(output_file, "w", newline="") as datafile:
        writer = csv.writer(datafile)
        writer.writerow(["Financial Analysis"])
        writer.writerow("---")
        writer.writerows(output)
 
    # -------------------------------------------------------------------
    # Print to Screen  
    # -------------------------------------------------------------------
    print("Financial Analysis")
    print("-"*25) 
    for x, y in zip(numbers, greatest): 
        print ((x, y)) 
  
print("--- The End ---")
  
  
 
   
   







