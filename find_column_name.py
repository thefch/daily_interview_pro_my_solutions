#date: 21/06/2020

# initialize alphabet list
MAX_COLUMN = 26
alphabet = [chr(i) for i in range(65,65+MAX_COLUMN,1)]


# return the length of the column name
def get_range(n):
    count = 1
    i = 0
    while True:
        # every 26 letters is one char-space
        if MAX_COLUMN+i >= n :
            return count 

        count += 1
        i += MAX_COLUMN
    
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
    
    # get columna name when >=26
    if n <= MAX_COLUMN:  
        return get(n)
    else:
        out = ''
        index = n
        for i in range(rounds) :
            
            # if modulo is 0, get the first letter
            # eg. 27 -> AA not ZA
            if index % MAX_COLUMN == 0:
                out += (get(MAX_COLUMN-MAX_COLUMN+i))
            else:
                out += (get(index-MAX_COLUMN))
                index -= n -MAX_COLUMN 
                
        # reverse string
        return out[len(out)::-1]
        
   
print(column_name(26))#Z
print(column_name(27))#AA
print(column_name(28))#AB
print(column_name(29))#AC
print(column_name(30))#AD
print(column_name(MAX_COLUMN))#Z
print(column_name(MAX_COLUMN*MAX_COLUMN-26))#AD

# needs to be corrected for these kind of values
# not sure the results
print(column_name(300))#???


