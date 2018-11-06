#dependencies
import os 
import csv
#path
csvpath = os.path.join("election_data.csv")
#read path using csv module
with open(csvpath, newline='') as csvfile
    read_election = csv.reader(csvfile, delimiter=',')
    skipheader = next(read_election)

#create list for total number of votes cast, candidates
total_votes = []
candidate_list = []
#create list for number of votes per candidate
votes_per_cand = []



