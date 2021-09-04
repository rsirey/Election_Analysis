#The data we need to retrieve
    # 1. The total number of votes cast
    # 2. A list of all candidates who recieved votes
    # 3. The total number of votes each candidate won.
    # 4. The percentage of total votes won by each candiate
    # 5. The winner of the election based on popular vote.

# Add our dependencies 
import csv
import os

#assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#assign a variable to  save the path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file
with open(file_to_load) as election_data:

    #To do: read and analyze data here 
    file_reader = csv.reader(election_data)

    #rear and print the header row
    headers = next(file_reader)
    print(headers)
    
   

#using the with statement open the  file as a text file 
with open(file_to_save, "w") as txt_file:

#write three counties to the file
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

