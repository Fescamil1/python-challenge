# imports os to create paths across operating systems and csv module for reading CSV files
import os
import csv

#set variables here
total_votes= 0
candidate_list=[]
cvotes_list=[]
cpercent_list=[]
#percent=0.0
maxPercent=0.0

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


# calculate the percentage per candidate /may need to create 3rd list
for x in range(len(candidate_list)):
    candidate_votes =int(cvotes_list[x])
    percent=(candidate_votes/total_votes)*100
    cpercent_list.append(percent) #add percentage to the list
    if percent > maxPercent:
        winnerIndex=x  #set the index for the winner to use later


print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")           
print("---------------------------")
#print the output of each list in oder f
for candidates in range(len(candidate_list)):
    print(f"{candidate_list[candidates]}: {cpercent_list[candidates]}% ({cvotes_list[candidates]}) ")
print("---------------------------")
print(f"Winner: {candidate_list[winnerIndex]}")
print("---------------------------")    