import csv

#variables
total_vot = 0
max_vot = 0
candidates = {}
win = ""

#read csv file
with open('election_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    
    for row in reader:
        total_vot += 1
        candidate = row[2]
        
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
            
#determine winner
for candidate, votes in candidates.items():
    perct = (votes / total_votes) * 100
    
    if votes > max_vot:
        max_vot = votes
        win = candidate
        
#print results
print("Election Results")
print("----------------")
print(f"Total Votes: {total_vot}")
print("-------------------")
for candidate, votes in candidates.items():
    print(f"{candidate}: {votes/total_vot * 100:.3f}% ({votes})")
print("-------------------------------------")
print(f"Winner: {winner}")
print("--------------------")

#export results to txt file
with open("election_results.txt", "w") as file:
    file.write("Election Results\n")
    file.write(f"Total Votes: {total_vot}\n")
    for candidate, votes in candidates.items():
        file.write(f"{candidate}: {votes/total_vot * 100:.3f}% ({votes})\n")
        file.write(f"Winner: {win\n}")
