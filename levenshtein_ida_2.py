# Informally, the Levenshtein distance between two words is 
# the minimum number of single-character edits (insertions, deletions or substitutions) 
# required to change one word into the other.

# The problem can be used for lexical similarity searching and identifying plagiarized text.

from datetime import datetime

string1 = "Mr. and Mrs. Dursley of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much."
string2 = "Mr. and Mrs. Potter of number five, Patriot Drive, were shy to say that they were imperfectly abnormal, thank you very much."


#####################
### SOLUTION NR 1 ###
#####################

# implementation of https://youtu.be/We3YDTzNXEk?si=veue2AH2XBAphjCE

def levenshtein_distance(s, t):
    # string lengths 
    m = len(s)
    n = len(t)

    # basis of the distance matrix
    d = [[0] * (n + 1) for i in range(m + 1)]  

    # initialize the first row and column of the matrix with integers starting from 0
    for i in range(1, m + 1):
        d[i][0] = i

    for j in range(1, n + 1):
        d[0][j] = j

    # calculate penalties between characters
    # the matrix represents all possible character pairs of the two strings
    # leaping through the pairs we assess if the elements of the pair are identical. 
    # if they're identical, then cost==0, else cost==1
    for j in range(1, n + 1): 
        for i in range(1, m + 1): 
            if s[i - 1] == t[j - 1]: 
                cost = 0
            else:
                cost = 1

            # insert penalties in matrix d, then asses the subset of the < 3 closest elements (2x2 matrix where the fourth element is in question)
            # if the cost is 0 (elements are identical) then we get the minimum of the 2x2 matrix, else we get minimum+1
            # iterate until we get the last element of matrix
            d[i][j] = min(d[i - 1][j] + 1,      # deletion
                          d[i][j - 1] + 1,      # insertion
                          d[i - 1][j - 1] + cost) # substitution   

    return d[m][n]

start_time = datetime.now()
l_dist = levenshtein_distance(string1, string2)
end_time = datetime.now()
print('Duration for solution 1: {}'.format(end_time - start_time))
print("Levenshtein Distance is " + str(l_dist))


###########################################
### SOLUTION NR 2 : dynamic programming ###
###########################################

from functools import lru_cache
# Least Recently Used (LRU) is a cache replacement algorithm that replaces cache when the space is full. 
# It allows us to access the values faster by removing the least recently used values.

def lev_dist(a, b):
    
    @lru_cache(None)  # for memorization
    def min_dist(s1, s2): 

        if s1 == len(a) or s2 == len(b):
            return len(a) - s1 + len(b) - s2

        # no change required
        if a[s1] == b[s2]:
            return min_dist(s1 + 1, s2 + 1)

        return 1 + min(
            min_dist(s1, s2 + 1),      # insert character
            min_dist(s1 + 1, s2),      # delete character
            min_dist(s1 + 1, s2 + 1),  # replace character
        )

    return min_dist(0, 0)

start_time = datetime.now()
l_dist_2 = lev_dist(string1, string2)
end_time = datetime.now()
print('Duration for solution 2: {}'.format(end_time - start_time))
print("Levenshtein Distance is " + str(l_dist_2))

