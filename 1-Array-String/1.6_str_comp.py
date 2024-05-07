'''
String Compression: Implement a method to perform basic string compression using the counts 
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the 
"compressed" string would not become smaller than the original string, your method should return 
the original string. You can assume the string has only uppercase and lowercase letters (a - z). 
'''

def str_comp(s: str):
    if not s: return ""
    res_arr = []
    prev_ch = s[0]
    count = 0

    for ch in s:
        if ch == prev_ch:
            count+=1
        else:
            res_arr.extend([prev_ch, count])
            prev_ch = ch
            count = 1

    res_arr.extend([prev_ch, count])
    res_str = "".join(map(str, res_arr))
    if len(res_arr) > len(s):
        return s
    return res_str



s1 = 'aaabbbccc'
print(f'for input - {s1}, the compressed string is: {str_comp(s1)}')