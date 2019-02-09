#PyPoll

import os
import csv

#change winner/print file

# -------------------------------------------------------------------
# Ooen file
# -------------------------------------------------------------------

file_path = os.path.join("election_data.csv")
with open(file_path,newline="")as csv_file:
        file_holder = csv.reader(csv_file, delimiter =",")
        next(file_holder)
# -------------------------------------------------------------------
# Loop through the file & calculate the info
# -------------------------------------------------------------------
        vote_id =""
        counter_vote = 0
        counter_total = 0
        candidate_di={} 
 
        for row in file_holder:
        
        # The total number of votes cast
                if row[0] != vote_id :
                        counter_vote= counter_vote +1
                        vote_id=row[0]
        
                        w= row[2]  
   
                if w in candidate_di:
                        candidate_di[w] = candidate_di[w] +1        
                else:
                        candidate_di[w] = 1        

        print("Election Results")
        list1 = ["Total Votes", counter_vote]

        print(f'Total Votes: {counter_vote}')
    
        # A complete list of candidates who received votes
        # The percentage of votes each candidate won  
        # The total number of votes each candidate won
        # The winner
        candidate_vote = 0
        
        output_file = os.path.join("output_file.csv")
        with open(output_file, "w", newline="") as datafile:
                writer = csv.writer(datafile)
                writer.writerow(["Election Results"])
                writer.writerow(["Total Votes:", counter_vote])
                
                for w in candidate_di:        
                        percentage = candidate_di[w]/counter_vote
                        x = "{0:.3%}".format(percentage)
                        #print(f'{w} { x } {candidate_di[w]}')
                        list2 = [w, x, candidate_di[w]]
                        print(f"{list2}")
                        writer.writerow(list2)         
                        if candidate_di[w] > candidate_vote:
                                winner = w  
                                candidate_vote = candidate_di[w]
                print(f'Winner:  {winner}')
                list3=["Winner:", winner]
                writer.writerow(list3) 
# -------------------------------------------------------------------
# Write to a newly created output file
# -------------------------------------------------------------------
  

#Election Results
#-------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -----------------


        print("--- The End ---")    
  
  
 
   
   







