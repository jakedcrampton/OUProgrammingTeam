# Definitely not the fastest solution but you know, I didn't ask for your opinion

from math import floor
from sys import stdin

# Count per-district votes
district_party_a = dict()
district_party_b = dict()
stdin.readline() # Ignore the first line because we know how to count
for precinct in stdin:
    (district, party_a, party_b) = tuple([int(x) for x in precinct.split()])
    
    if district not in district_party_a:
        district_party_a[district] = 0
    district_party_a[district] += party_a
    
    if district not in district_party_b:
        district_party_b[district] = 0
    district_party_b[district] += party_b

# Calculate wasted votes
w_a = 0
w_b = 0
votes = 0
for i in range (1, len(district_party_a) + 1):
    a_votes = district_party_a[i]
    b_votes = district_party_b[i]
    votes += a_votes + b_votes
    minimum_votes = floor((a_votes + b_votes) / 2) + 1

    # Please excuse the vague variable naming
    if a_votes > b_votes:
        wasted = a_votes - minimum_votes
        w_a += wasted
        w_b += b_votes
        print('A %s %s' % (wasted, b_votes))
    else:
        wasted = b_votes - minimum_votes
        w_b += wasted
        w_a += a_votes
        print('B %s %s' % (a_votes, wasted))

# Output the efficiency gap
print(abs(w_a - w_b)/votes)