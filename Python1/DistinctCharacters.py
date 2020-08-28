
#Return a dictionary whose keys are the strings of the input list and the corresponding values are the numbers of distinct characters in the key.

def distinct_characters(Lista1):
    s = {}
    for i in Lista1:
        s[i] = len(set(i))
    return s


print(distinct_characters(["check", "look", "try", "pop"]))