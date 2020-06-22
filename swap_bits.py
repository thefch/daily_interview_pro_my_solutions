# date: 18/06/2020

# Description:
# Given a 32-bit integer, 
# swap the 1st and 2nd bit,
# 3rd and 4th bit, up til the 31st and 32nd bit.

# convert from decimal to binary
def convert_to_binary(num):
    result=''
    while num != 0:
        remainder = num % 2  # gives the exact remainder
        num = num // 2
        result = str(remainder) + result
    return result

# swap 0s with 1s
def swap_bits(num):
    results = list(convert_to_binary(num))
    out =''
    for i in range(len(results)):
        if results[i] == '1':
            out += '0'
        else:
            out += '1'

    return '0b'+out

print(f"{swap_bits(0b10101010101010101010101010101010)}")

