# Qns: https://inventwithpython.com/bigbookpython/project24.html

import sys

print("Enter a number to factor (or 'QUIT' to quit):")

while True:
    user_num = input("> ")
    if user_num.isdecimal() and int(user_num) > 0:    # check for integer values > 0 
        break
    elif user_num.upper() == "QUIT":
        sys.exit()
    else: 
        print("Invalid input. Please input an integer > 0")
    
user_num = int(user_num)
start = 1       # 0 is usually not considered to be a factor 
end = user_num
factors = []

while start <= end:
    if user_num % start == 0:
        if start not in factors: 
            factors.append(start)
            factors.append(user_num // start)
        end = user_num // start         # Reduce searching range once factors are found 
    start += 1

factors.sort()

for index, factor in enumerate(factors): 
    factors[index] = str(factor)
    
print(", ".join(factors))