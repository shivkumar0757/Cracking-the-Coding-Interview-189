'''
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string 
has sufficient space at the end to hold the additional characters, and that you are given the "true" 
length of the string. (Note: If implementing in Java, please use a character array so that you can 
perform this operation in place.) 
EXAMPLE 
Input:  "Mr John Smith " , 13
Output: "Mr%20John%20Smith"
'''


def urlify(s: str, n: int):
    SPACE = " "
    SPACE_REPLACE = "%20"
    char_arr = list(s)


    for i in range(n):
        if char_arr[i] == SPACE:
            char_arr[i] = SPACE_REPLACE
    return "".join(char_arr[:n])



print(urlify("Mr John Smith " , 13))