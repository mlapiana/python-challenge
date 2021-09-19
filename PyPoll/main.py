import os
import csv


csvpath = os.path.join('Resources', 'election_data.csv')

totalvotes = 0
candidate = []
candidate_vote_count = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
       
        totalvotes += 1
        candidate_in = (row[2])
        
        if candidate_in in candidate:
            candidate_index = candidate.index(candidate_in)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
            candidate.append(candidate_in)
            candidate_vote_count.append(1)


pct = []
max_votes = candidate_vote_count[0]
max_index = 0

for x in range(len(candidate)):
    #calculation to get the percentage, x is the looper value
    vote_pct = round(candidate_vote_count[x]/totalvotes*100, 2)
    pct.append(vote_pct)
    
    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x

election_winner = candidate[max_index] 

print('Election Results')
print('-------------------------')
print(f'Total Votes: {totalvotes}')
print('-------------------------')
for x in range(len(candidate)):
    print(f'{candidate[x]} : {pct[x]}% ({candidate_vote_count[x]})')
print('-------------------------')
print(f'Election winner: {election_winner.upper()}')
print('-------------------------')

output_file = os.path.join('analysis', "pypoll_election_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('Election Results\n')
    datafile.write('-------------------------\n')
    datafile.write(f'Total Votes: {totalvotes}\n')
    datafile.write('-------------------------\n')
    for x in range(len(candidate)):
        datafile.write(f'{candidate[x]} : {pct[x]}% ({candidate_vote_count[x]})\n')
    datafile.write('-------------------------\n')
    datafile.write(f'Election winner: {election_winner.upper()}\n')
    datafile.write('-------------------------\n')

