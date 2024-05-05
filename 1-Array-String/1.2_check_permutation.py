# Check Permutation: Given two strings, write a method to decide if one is a permutation of the 
# other. 


# Sort the strings and then compare these, assume we will not skip any character
def check_permutation_sort(s1:str, s2:str):
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)

    return s1_sorted == s2_sorted


# Assuming we have ascii 2 characters, and not skipping any character
def check_permutation_freq(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    
    char_freqs = [0] * 128

    for i in range(len(s1)):
        s1_ind = ord(s1[i])
        char_freqs[s1_ind] += 1

        s2_ind = ord(s2[i])
        char_freqs[s2_ind] -= 1
    
    for freq in char_freqs:
        if freq != 0:
            return False
    return True
    

s1 = 'abcde'
s2 = 'bcdae'

print(f"res for sorted: {check_permutation_sort(s1, s2)}")
print(f"res for frequency: {check_permutation_freq(s1, s2)}")
