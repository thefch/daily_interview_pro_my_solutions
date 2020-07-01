# date: 02/09/2019

# Description:
# You are given a string of parenthesis.
# Return the minimum number of parenthesis 
# that would need to be removed in order to 
# make the string valid.

# if is the open parenthesis
def is_open(c):
    return c == '('

# check if the subsequent parenthesis is the correct one
def check_next(s,i,needs_next):
    if s[i] == needs_next:
        return True
    return False

def count_invalid_parenthesis(s):
    # next required parenthesis
    needs_next = ''
    count = 0
    for i in range(len(s)-1):
        if is_open(s[i]):
            needs_next = ')' 
        else:
            needs_next = '('
            
        # is not correct when the next parenthesis is not
        # the correct one and when is not an open parenthesis
        # eg. ((()) -> 1 missing close parenthesis
        if not check_next(s,i+1,needs_next) and not is_open(s[i]):
            count += 1

        # case when the string starts
        # with an open parenthesis and continues with a closed one
        # eg. )( -> 2 missing parenthesis
        # eg. )) -> 2 missing parenthesis
        if i==0 and not is_open(s[i]):
            count += 1
    return count
    

print(count_invalid_parenthesis("(()())()"))
# 1
