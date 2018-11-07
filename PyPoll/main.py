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
#create lists comprised only of votes for each candidate
Khan = []
Correy = []
Li = []
Otooley = []
for i in candidate_raw_list:
    if i == str(candidate_short[0]):
        Khan.append(i)
    elif i == str(candidate_short[1]):
        Correy.append(i)
    elif i == str(candidate_short[2]): 
        Li.append(i)
    else:
        Otooley.append(i)
Khan_total = int(len(Khan))
Correy_total = int(len(Correy))
Li_total = int(len(Li))
Otooley_total = int(len(Otooley))
Khan_percent = Khan_total/(len(candidate_raw_list))*100
Correy_percent = Correy_total/(len(candidate_raw_list))*100
Li_percent = Li_total/(len(candidate_raw_list))*100
Otooley_percent = Otooley_total/(len(candidate_raw_list))*100

#to find a winner, make a dictionary
votelist = [Khan_total, Correy_total, Li_total, Otooley_total]
zip_candidates_votes = dict(zip(candidate_short, votelist))
winner = max(zip_candidates_votes, key=zip_candidates_votes.get)

#print table
print(f"Election Results")
print(f"Total Votes: {len(candidate_raw_list)}")
print(f"Khan: {Khan_percent:.3f}% ({Khan_total})")
print(f"Correy: {Correy_percent:.3f}% ({Correy_total})")
print(f"Li: {Li_percent:.3f}% ({Li_total})")
print(f"O'Tooley: {Otooley_percent:.3f}% ({Otooley_total})")
print(f"Winner: {winner}")

#generate text files
output_path = os.path.join("PyPoll_Analysis.txt")
with open(output_path, "w") as csvfile:
    writer = csv.writer(csvfile)
    #First row
    writer.writerow(["Election Results"])
    #Second row
    writer.writerow([f"Total Votes: {len(candidate_raw_list)}"])
    writer.writerow([f"Khan: {Khan_percent:.3f}% ({Khan_total})"])
    writer.writerow([f"Correy: {Correy_percent:.3f}% ({Correy_total})"])
    writer.writerow([f"Li: {Li_percent:.3f}% ({Li_total})"])
    writer.writerow([f"O'Tooley: {Otooley_percent:.3f}% ({Otooley_total})"])
    writer.writerow([f"Winner: {winner}"])






