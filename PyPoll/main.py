from itertools import count
import os
import csv
import sys

os.chdir(sys.path[0])
csvpath = os.path.join('Resources', 'election_data.csv')

ballot_id = []
candidate_dict = {}


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    firstrow = next(csvreader)
    for row in csvreader:
        ballot_id.append(row[0])

        candidate_name = row[2]
        if candidate_name not in candidate_dict:
            candidate_dict[candidate_name] = 1
            
        else:
            candidate_dict[candidate_name] = candidate_dict[candidate_name] + 1


print(f"Election Results")

print(f"----------------")

print(f"Total Votes: {len(ballot_id)}")

print(f"----------------")

for candidate_name in candidate_dict:
    candidate_votes = candidate_dict[candidate_name]
    candidate_perc = (candidate_votes / len(ballot_id))
    election_winner = max(candidate_dict, key=candidate_dict.get)

    print(f"{(candidate_name)}: {(candidate_perc):.3%} ({(candidate_votes)})")

print(f"----------------")

print(f"Winner: {election_winner}")

print(f"----------------")