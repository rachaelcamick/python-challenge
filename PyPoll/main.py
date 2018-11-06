#dependencies
import os 
import csv
#path
csvpath = os.path.join("election_data.csv")
#read path using csv module
with open(csvpath, newline='') as csvfile
    read_election = csv.reader(csvfile, delimiter=',')

#create list for total number of votes cast, candidates
total_votes = []
candidate_list = []
#create list 

