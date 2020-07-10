# date: 09/07/2020

# Description:
# Given a string, we want to remove 2 adjacent characters that are the same, 
# and repeat the process with the new string until we can no longer perform the operation.


def remove_adjacent_dup(s):
    finished = False
    
    index = 0
    while not finished:
        if s[index+1]==s[index]:
            s = s.replace(s[index+1],'')
            index = 0
        else:
            index +=1 
        if index+1 > len(s)-1:
            finished = True
    return s
    
    
    
    

print(remove_adjacent_dup("cabba"))
# Start with cabba
# After remove bb: caa
# After remove aa: c
# print c
