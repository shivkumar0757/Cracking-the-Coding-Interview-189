# Problem statement
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you 
# cannot use additional data structures? 


# Bruteforce , using 2 loops i and j

def is_unique_bf(s:str):
    if not s: return True

    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True

# Usning char array to store if the char has occured?
def is_unique_arr(s: str):
    if len(s) > 128: return False
    char_present = [False] * 128   #As we can have 0-127 characters in ascii 2
    for chr in s:
        chr_ind = ord(chr)
        if char_present[chr_ind]:
            return False
        char_present[chr_ind] = True
    return True


print("testing our BF and optimised approach")
s1 = 'abcdefgh'
s2 = 'abd@jakjkjk@'

print(f'res for bf, str: {s1}, is unique? : ', is_unique_bf(s1))
print(f'res for bf, str: {s2}, is unique? : ', is_unique_bf(s2))

print(f'res for optimised, str: {s1}, is unique? : ', is_unique_arr(s1))
print(f'res for optimised, str: {s2}, is unique? : ', is_unique_arr(s2))


