from itertools import count
import os
import csv
import sys

os.chdir(sys.path[0])
csvpath = os.path.join('Resources', 'election_data.csv')

ballot_id = []
candidate_dict = {}
headers = []


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    # Read and store headers
    headers = next(csvreader)
    for row in csvreader:
        ballot_id.append(row[0])

        candidate_name = row[2]
        if candidate_name not in candidate_dict:
            candidate_dict[candidate_name] = 1
            
        else:
            candidate_dict[candidate_name] = candidate_dict[candidate_name] + 1

# Open analysis file to write to and create if does not exist
analysis_path = os.path.join('analysis', 'pypoll_analysis.txt')
with open(analysis_path, 'w') as analysis_file:
    analysis_file.write(f"Election Results \n")
    print(f"Election Results")

    analysis_file.write(f"---------------- \n")
    print(f"----------------")

    analysis_file.write(f"Total Votes: {len(ballot_id)} \n")
    print(f"Total Votes: {len(ballot_id)}")

    analysis_file.write(f"---------------- \n")
    print(f"----------------")


    for candidate_name in candidate_dict:
        #Number of votes for the candidate
        candidate_votes = candidate_dict[candidate_name]
        #Percent of the votes
        candidate_perc = (candidate_votes / len(ballot_id))

        analysis_file.write(f"{(candidate_name)}: {(candidate_perc):.3%} ({(candidate_votes)}) \n")
        print(f"{(candidate_name)}: {(candidate_perc):.3%} ({(candidate_votes)})")

    analysis_file.write(f"---------------- \n")
    print(f"----------------")

    #Calculate winner by finding candidate with max votes
    election_winner = max(candidate_dict, key=candidate_dict.get)
    analysis_file.write(f"Winner: {election_winner} \n")
    print(f"Winner: {election_winner}")

    analysis_file.write(f"---------------- \n")
    print(f"----------------")