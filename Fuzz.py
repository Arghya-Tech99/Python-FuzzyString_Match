from rapidfuzz import fuzz, process
# rapidfuzz - built using C++; faster and more efficient

s1 = "demo string one, for fuzzy string matching"
s2 = "something completely different for demo purpose"

print(fuzz.ratio(s1,s2))

'''
fuzz.ratio(s1,s2) functionality:-
    1. Calculates Levenshtein distance between s1 and s2
    2. Converts that distance into a similarity ratio, expressed as a percentage
'''
