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

#nitialize a total vote counter 
total_votes = 0

#declare a candidate list
candidate_options = []

#create candiate/vote dictionary
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:

    #To do: read and analyze data here 
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    
    #print each row in the CSV file
    for row in file_reader:
        #add to the total vote count
        total_votes += 1

        #print the candidate name from each row.
        candidate_name = row[2]

        #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            #add it to the list of candidates
            candidate_options.append(candidate_name)

            #begin tracking  that candidate's vote count
            candidate_votes[candidate_name] = 0

        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#determine the percentage of votes for each candidate by looping through the counts
#1. iterate  through the candidate list
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        #print out each candidates name, vote count, and percentage of votes to the terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


        #determine winning vote count and candidate
        #determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning_count = votes and winning percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #and set the winning_candidate equal tothe candidates name
            winning_candidate = candidate_name

    #print out the winning candidate, vote count and percentage to terminal 
    winning_candidate_summary = (
        f"-------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------------\n")
    print(winning_candidate_summary)




#print candidate vote dictionary
print(candidate_votes)
        

    
   

#using the with statement open the  file as a text file 
with open(file_to_save, "w") as txt_file:

#write three counties to the file
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

