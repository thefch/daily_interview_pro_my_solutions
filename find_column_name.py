#date: 21/06/2020

# Description:
# In many spreadsheet applications, the columns are marked with letters. 
# From the 1st to the 26th column the letters are A to Z. 
# Then starting from the 27th column it uses AA, AB, ..., ZZ, AAA, etc
# Given a number n, find the n-th column name.


# initialize alphabet list
MAX_COLUMN = 26
alphabet = [chr(i) for i in range(65,65+MAX_COLUMN,1)]


# return the length of the column name
def get_range(n):
    count = 0
    while True:
        count += 1
        # every 26 letters is one char-space
        if n <= MAX_COLUMN:
            return count

        n = reduce(n)

# return the letter from the alphabet
def get(n):
    # find the letter if index is more than 26
    while n > MAX_COLUMN:
        n = reduce(n)
    return alphabet[n-1]

def reduce(n):
    return n- MAX_COLUMN

    
def column_name(n):        
    print('\nn:',n)
    rounds = get_range(n)
    print('rounds:',rounds)
    
    # get column name when >=26
    if n <= MAX_COLUMN:  
        return get(n)
    else:
        out = ''
        index = n
        for i in range(rounds) :
            out += get(n-MAX_COLUMN)
            if n < 26:
                out += get(0)
                break

            # if index <=26 : 

            #     out += get(MAX_COLUMN-MAX_COLUMN+i)
            # else:
            #     out += get(MAX_COLUMN-MAX_COLUMN+i)

            # index -= n -MAX_COLUMN 

            # if modulo is 0, get the first letter
            # eg. 27 -> AA not ZA
            # if index % MAX_COLUMN == 0:
            #     out += get(MAX_COLUMN-MAX_COLUMN+i)
            # else:
            #     out += get(index-MAX_COLUMN)
            #     index -= n -MAX_COLUMN 
                
        # reverse string
        return out[len(out)::-1]
        
   
# print(column_name(26))#Z
# print(column_name(27))#AA
# print(column_name(28))#AB
# print(column_name(29))#AC
# print(column_name(30))#AD
# print(column_name(MAX_COLUMN))#Z
# print(column_name(MAX_COLUMN*MAX_COLUMN-26))#

# for i in range(0,30,1):
#     print(column_name(i))

# needs to be corrected for these kind of values
# not sure the results
# print(column_name(300))#???


for i in range(0,MAX_COLUMN*MAX_COLUMN,1):
    print('i:',i,' ',get_range(i))