import csv
read_csv = csv.DictReader(open('data/president_county_candidate.csv')) 

total = 0
candidates = {}
states = {}
counties = {}
parties = {}
winers = {}


for row in read_csv:

    total += 1
    party = row['party']
    state = row['state']
    county = row['county']
    candidate = row['candidate']
    win = row['won']

    if state not in states.keys():
        states[state] = 0

    if county not in counties.keys():
        counties[county] = 0

    if party not in parties.keys():
        parties[party] = 0

    if candidate not in candidates.keys():
        candidates[candidate] = 0

    if win not in winers.keys():
        winers[win] = 0

    states[state] = 0
    parties[party] = 0
    counties[county] = 0
    candidates[candidate] = 0

output = f'''
=====================PRESIDENTIAL=ANALYSIS=2020====================
\nTotal rows: {total}
Total candidates: {len(candidates)}
Total states: {len(states)}
Total counties: {len(counties)}
Total parties: {len(parties)}

'''



print(output)