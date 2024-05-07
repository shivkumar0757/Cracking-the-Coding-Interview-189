'''One Away: There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. Given two strings, write a function to check if they are 
one edit (or zero edits) away. 
EXAMPLE 
pale, ple -> true 
pales, pale -> true 
pale, bale -> true 
pale, bae -> false 
'''

def one_away(first: str, second: str):
    if len(first) == len(second):
        return one_edit_replace(first, second)
    if len(first) - 1 == len(second):
        return one_edit_insert(second, first)
    if len(first) +1 == len(second):
        return one_edit_insert(first, second)
    return False

def one_edit_replace(s1, s2):
    diff = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if diff:
                return False
            diff = True

    return True

def one_edit_insert(s1, s2):
    index1 = 0
    index2 = 0
    while index1 < len(s1)  and index2<len(s2):
        if s1[index1] == s2[index2]:
            index1 += 1
            index2 += 1
            continue
        if index1 != index2:
            return False
        index2+=1

    return True
        
def one_away_single(first: str, second: str):
    if abs(len(first) - len(second)) > 1:
        return False
    
    s1, s2 = (first, second) if len(first) < len(second) else (second, first)
    found_diff = False
    ind1 = 0
    ind2 = 0

    while ind1 < len(s1) and ind2 < len(s2):
        if s1[ind1] == s2[ind2]:
            ind1 += 1
            ind2 += 1
            continue

        if found_diff:
            return False
        found_diff = True
        if len(s1) == len(s2):
            ind1 += 1
        ind2 += 1

    return True

def one_away_char(first: str, second: str):
    # If the lengths of the strings differ by more than 1, return False
    if abs(len(first) - len(second)) > 1:
        return False

    # Assign the shorter and longer strings to s1 and s2 respectively
    s1, s2 = (first, second) if len(first) < len(second) else (second, first)

    # Iterate over both strings simultaneously
    for i, char in enumerate(s1):
        # If characters at current position are different
        if char != s2[i]:
            # If lengths are equal, the rest of the strings after this position should be the same
            # If lengths are not equal, the rest of the strings starting from the next position in the longer string should be the same
            return s1[i+1:] == s2[i+1:] if len(s1) == len(s2) else s1[i:] == s2[i+1:]

    # If no difference was found, the strings are one edit away from each other
    return True

s1 = 'abcd'
s2 = 'abcdd'
print(one_away(s1, s2))

print(one_away_single(s1, s2))

print(one_away_char(s1, s2))

