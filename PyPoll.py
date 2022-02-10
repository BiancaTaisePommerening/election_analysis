# The data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote




# INDIRECT PATH TO FILE
from calendar import c
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# WRITE TO FILE using the 'with' statement.
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initializing a variable called total_votes set to zero.
total_votes = 0

# Declaring a new list.
candidate_options = []

# Declare an empty dictionary.
candidate_votes = {}

# Winning candidate and winning count tracker.
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
  

 # Read and Print the header row.
    headers = next(file_reader)

   # Using a for loop.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        #Print the candidate name from each row.
        candidate_name = row[2]

# If the candidate does not match any existing cadidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidtes.
            candidate_options.append(candidate_name)
            
            # we're setting each candidate's vote count to zero. Once we set it to zero, then we can start tallying the votes for each candidate.
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

            # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# save the results to the text file.
with open(file_to_save, "w") as txt_file:

    # DESCRIBING THE BLOCK OF CODE BELOW.
    # The variable election_results, has 4 strings. The first string, Election Results, has the newline character, \n, before and after it.
    # When this line is saved to the text file or printed, it will be on the second line; then a newline is created.
    # The second string is going to be printed on the third line, with 25 dashes, and then a new line is created.
    # The third string is going to be printed on the fourth line, 
            # where Total Votes: {total_votes:,} will be printed with the votes formatted with a thousands separator, and then a newline is created.
    #The fourth string is going to be printed on the fifth line, with 25 dashes, and then a new line is created.
    # Then, we print the election_results, with the parameter end="" equal to an empty string. The "end" parameter is added to ensure that nothing will be printed on the last line when the election_results.
            # Anything code that is printed after print(election_results, end="") will be printed on a newline.
    # Finally, we write elction_results to the text file.

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")  
    print(election_results, end ="")
    txt_file.write(election_results)


    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
     
        # print out each candidate's name, vote count, and percentage of votes to the terminal.
        print(candidate_results)
        # Save the candidate result to our txt file.
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage = vote_percentage.
            winning_count  = votes 
            winning_percentage = vote_percentage 
            # Set the winning_candidate euqal to the candidate's name.
            winning_candidate = candidate_name


    winning_candidate_summary = (

        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count:,}\n"
        f"Winning percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")  
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)


    # print out the winning candidate count, vote and percentage to terminal.
    # print(f"{winning_candidate}: received {winning_count}: votes, which represents {winning_percentage: .1f}% of the total votes.")








