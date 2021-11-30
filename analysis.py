import csv
read_csv = csv.DictReader(open('data/president_county_candidate.csv')) 

total = 0
candidates = {}
states = {}
counties = {}
parties = {}
winers = {}

for row in read_csv:

    party = row['party']
    state = row['state']
    county = row['county']
    candidate = row['candidate']
    votes = row['total_votes']
    win = row['won']

    if candidate not in candidates.keys():
        candidates[candidate] = {}

    # if state not in states.keys():
    candidates[candidate]['party'] = party

    if 'state' not in candidates[candidate]:
        candidates[candidate]['state'] = {}
    
    if state not in candidates[candidate]['state']:
        candidates[candidate]['state'][state] = {}

    if county not in  candidates[candidate]['state'][state]:
         candidates[candidate]['state'][state][county] = {}

    candidates[candidate]['state'][state][county]['votes'] = votes    
    candidates[candidate]['state'][state][county]['won'] = win    

output = f'''
=====================PRESIDENTIAL=ANALYSIS=2020====================
Total candidates: {len(candidates)}
candidates: 
===================================================================
{[ cand for cand in candidates.keys() ]}
===================================================================

'''

for cand in candidates.keys():
    party = candidates[cand]['party']
    
    for sta in candidates[cand]['state']:
                
        output += f'\tCandidate: {cand} \tParty: {party} \n\n'
        state_votes = 0
        cty_won = 0
        output += f'\t\tVOTES\tWON\tCOUNTY'
        output += '\n===================================================================\n'
        for cty in  candidates[cand]['state'][sta]:
            votes = int(candidates[cand]['state'][sta][cty]['votes'])
            status = candidates[cand]["state"][sta][cty]["won"]
            
            if votes:
                output += f'\t\t{votes}'
                state_votes += votes
                output += f'\t{status}\t{cty}\n'
            
            if status == True:
                cty_won += 1
            
        output += '===================================================================\n'
        output += f'{sta}\t{state_votes} \t{cty_won}'
        output += '\n===================================================================\n\n\n'

                
print(output)