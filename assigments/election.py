# Assignment simulate elections page 257

# 2 Candidates A and B

# Candidate A has following odds:
# 87% change of winning in region 1
# 65% changes of winning in region 2
# 17% changes of winning in region 3

from random import random

candidate_a_won = 0
candidate_b_won = 0

for i in range(0, 10000):
    result = random()
    candidate_a = 0
    candidate_b = 0
    if result + .87 >= 1:
        candidate_a += 1
    else:
        candidate_b += 1
    if result + .65 >= 1:
        candidate_a += 1
    else:
        candidate_b += 1
    if result + .17 >= 1:
        candidate_a += 1
    else:
        candidate_b += 1
    if candidate_a > candidate_b:
        candidate_a_won += 1
    else:
        candidate_b_won += 1

print('Candidate A won elections {} times, candidate B won elections {} times'.format(candidate_a_won, candidate_b_won))
