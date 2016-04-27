# Fatto da Davide Barbini

import statistics as stats

def average(nlist=[]):
    return stats.mean(nlist)

def mode(nlist=[]):
    return stats.mode(nlist)

def median(nlist=[]):
    return stats.median(nlist)


nlist = [0, 0, 6]

print(mode(nlist))
print(median(nlist))
print(average(nlist))
