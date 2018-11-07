# dependencies
import os 
import csv
#path
csvpath = os.path.join("election_data.csv")
#create list for total number of votes cast, candidates
candidate_raw_list = []
#create list for number of votes per candidate
votes_per_cand = []
#read path using csv module
with open(csvpath, newline='') as csvfile:
    read_election = csv.reader(csvfile, delimiter=',')
    skipheader = next(read_election)
    # loop through csvfile for total number of votes
    for row in read_election:
        candidate_raw_list.append(row[2])
candidate_short = []    
for candidate in candidate_raw_list:
    if candidate not in candidate_short:
        candidate_short.append(candidate)







