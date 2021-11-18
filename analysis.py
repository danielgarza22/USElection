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
{[ cand  for cand in candidates.keys() ]}
===================================================================

'''
for cand in candidates.keys():
    output += cand
    output += '\nParty: ' + candidates[cand]['party'] + '\nStates:\n\n'

    can_states = []
    for loc in candidates[cand]['state']:
        output+=loc
        output += '\n===================================================================\n'

        if loc not in can_states:
            can_states.append(loc)

    
    for sta in can_states:
        for cty in candidates[cand]['state'][sta]:
            if int(candidates[cand]['state'][sta][cty]['votes']):      
                output+='\t' + cty
                output+='\n\tVOTES: ' + candidates[cand]['state'][sta][cty]['votes']      
                output+='\n\tWON: ' + candidates[cand]['state'][sta][cty]['won']      
                output += '\n\t===================================================================\n'
        
print(output)