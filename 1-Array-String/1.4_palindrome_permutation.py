'''Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin
 drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation 
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. 
EXAMPLE 
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
'''

from collections import Counter

def is_palindromic_permutation(s: str):
    s = "".join(s.lower().split())
    char_freq = Counter(s)

    odd_freq_count = sum(freq % 2 for freq in char_freq.values())

    return odd_freq_count < 2

def palindromic_permutation(s: str):
    s = s.lower()
    even_freq_arr = [True] * 128
    for ch in s:
        if ch == " ":
            continue
        ch_ind = ord(ch)
        
        even_freq_arr[ch_ind] = not even_freq_arr[ch_ind]

    false_count  = 0
    for is_false_count in even_freq_arr:
        if not is_false_count:
            false_count += 1
    return false_count < 2


# Single pass to store odd count
def palind_perm_single(s: str):
    freq_arr = [0] * 128
    s=s.lower()
    odd_count = 0
    for ch in s:
        if ch == ' ':
            continue
        freq_arr[ord(ch)]+=1
        if freq_arr[ord(ch)] %2 != 0:
            odd_count+=1
        else:
            odd_count-=1
    return odd_count < 2        

s = "Tact Coa"
print(is_palindromic_permutation(s))
print(palindromic_permutation(s))
print(palind_perm_single(s))


print('----- case 2 not pal perm')
s1 = 'aabc'
print(is_palindromic_permutation(s1))
print(palindromic_permutation(s1))
print(palind_perm_single(s1))

