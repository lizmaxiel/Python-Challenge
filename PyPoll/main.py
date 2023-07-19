# Dependencies
import csv
import os

# Getting to the current directory
current_directory = os.path.dirname(__file__)

# Path to the election data csv file
election_data_path = os.path.join(current_directory, 'resources', 'election_data.csv')

# Applying variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Reading the election data csv file
with open(election_data_path, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    header = next(csvreader)  

    # Counts the votes and tallies the candidates
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculates the percentage of votes and find the winner
results = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, percentage, votes))

    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Prints the election results to terminal
print("Election Results")
print("--------------------")
print(f"Total Votes: {total_votes}")
print("--------------------")
for result in results:
    candidate, percentage, votes = result
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("--------------------")
print(f"Winner: {winner}")
print("--------------------")

# Defining the path to the output text file
output_file_path = os.path.join(current_directory, 'analysis', 'results.txt')

# Exporting the election analysis results to a text file
with open(output_file_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for result in results:
        candidate, percentage, votes = result
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")

# Prints a message indicating the successful export of the results
print(f"Results exported to: {output_file_path}")