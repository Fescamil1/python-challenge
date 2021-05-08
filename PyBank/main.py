 
# imports os to create paths across operating systems and csv module for reading CSV files
import os
import csv

#add variables
month_count=0
#profit_loss_count=["", 0]  #change it to list to capture see if it fixes average count results
profit_loss_count=0
gprofit=0
gloss=0
change=0

#create a list to capture changes
change_list=[]
previous_plrev=0 #set starting point for capturing the previous profit/lost

# Specify the file to read from
csvpath = os.path.join('Resources', 'budget_data.csv')

# Specify the file to write to
output_path = os.path.join("analysis", "PyBankAnalysis.txt")

with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read and Skip the header row first 
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        
        if month_count ==0:
            previous_plrev=float(row[1]) #dont calculate change for 1st month
        else:
            #calculate change in profit/loss revenue and add it to the list starting with month 2
            change = float(row[1])-previous_plrev
            change_list.append(change)
            #change_list= change_list + [change]
            previous_plrev=float(row[1])
        
        #increase month count and Total
        month_count+=1 
        profit_loss_count+= int(row[1])

        #find greatest values
        if change > gprofit:
            gprofit =change
            pday = row[0]
        if change < gloss:
            gloss=change
            lday=row[0]
       

#calcuate average change after         
avg_change=round((sum(change_list)/len(change_list)),ndigits=2)

#print to Terminal
print("Financial Analysis")
print("-------------------------------")
print(f"Total months : {month_count}")
print(f"Total: ${profit_loss_count}")
print(f"Average change: {avg_change}") #fix this 
print(f"Greatest Increase in Profits: {pday} (${int(gprofit)})")
print(f"Greatest Decrease in Profits: {lday} (${int(gloss)})")

#write to outputfile: 
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------------\n")
    file.write(f"Total Months : {month_count} \n")
    file.write(f"Total: ${profit_loss_count}\n")
    file.write(f"Average Change: {avg_change}\n") 
    file.write(f"Greatest Increase in Profits: {pday} (${int(gprofit)})\n")
    file.write(f"Greatest Decrease in Profits: {lday} (${int(gloss)})\n")