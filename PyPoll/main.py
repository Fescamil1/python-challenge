# imports os to create paths across operating systems and csv module for reading CSV files
import os
import csv

#set variables here
total_votes= 0
candidate_list=[]
cvotes_list=[]
cpercent=0.0


#Specify the file to read from
csvpath = os.path.join('Resources', 'election_data.csv')

# Specify the file to write to
output_path = os.path.join("analysis", "PyPollAnalysis.txt")

with open(csvpath) as csvfile:    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read and Skip the header row first 
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        total_votes += 1 #increase total counts
        candidate = row[2]
        #if candidate name is in the list add to its vote count, else add their name and start count
        if candidate in candidate_list:      
            cindex =candidate_list.index(candidate) #find the index for the candidate name and use it to increase vote count
            cvotes_list[cindex]+=1
        else:
            candidate_list.append(candidate)
            cvotes_list.append(1) #give the newly added candidate 1 vote

print(candidate_list, cvotes_list)
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")           
print("---------------------------")
    