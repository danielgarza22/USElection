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
    win = row['won']

    if candidate not in candidates.keys():
        candidates[candidate] = {}

    # if state not in states.keys():
    candidates[candidate]['party'] = {
        party: {
            'state':{
                state:{
                    'county':{
                        county:{
                            'votes': row['total_votes'],
                            'won':row['won']
                            }
                        }
                    }
                }
            }
        }


output = f'''
=====================PRESIDENTIAL=ANALYSIS=2020====================
Total candidates: {len(candidates)}
candidates: 
===================================================================
{[ cand  for cand in candidates.keys() ]}
===================================================================


'''
# Total states: {len(states)}
# Total counties: {len(counties)}
# Total parties: {len(parties)}



print(output)