import os
import csv

total_votes = []
candidates = []
candidate_votes = []
vote_percent = []
popular_vote = 0

csvpath = os.path.join('Resources', 'election_data.csv')
txtpath = os.path.join('Analysis', 'Analysis.txt')
analysis_output = open("Analysis/Analysis.txt","w")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes.append(row[2])

    total_votes.sort()

    candidates = set(total_votes)
    candidates = list(candidates)
    
    for x in candidates:
        candidate_votes.append(total_votes.count(x))
     
    for x in candidate_votes:
        vote_percent.append(round(((x / len(total_votes)) * 100),3))
    
    print("Election Results")
    analysis_output.write("Election Results\n")
    print("------------------------------------------")
    analysis_output.write("------------------------------------------\n")

    print("Total Votes:" + str(len(total_votes)))
    analysis_output.write("Total Votes:" + str(len(total_votes)) + "\n")
    
    print("------------------------------------------")
    analysis_output.write("------------------------------------------\n")

    x=0
    while (x < len(candidates)):
        print(candidates[x] + ": " + str(vote_percent[x]) + "% " + "(" + str(candidate_votes[x]) + ")")
        analysis_output.write(candidates[x] + ": " + str(vote_percent[x]) + "% " + "(" + str(candidate_votes[x]) + ")\n")
        x += 1

    print("------------------------------------------")
    analysis_output.write("------------------------------------------\n")

    n=0
    while (n < len(candidates)):
        if candidate_votes[n] > popular_vote:
            popular_vote = candidate_votes[n]
        n += 1
    print("Winner: " + candidates[candidate_votes.index(popular_vote)])
    analysis_output.write("Winner: " + candidates[candidate_votes.index(popular_vote)] + "\n")

    print("------------------------------------------")
    analysis_output.write("------------------------------------------\n")