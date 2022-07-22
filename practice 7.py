"""
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""

check = input( "please type a string -->  ")

forward = [] 
backward = [] 

# can also add something to remove the spaces to check for palindrome, but just another for loop 
for i in check:
    forward.append(i)
    backward.append(i)
backward.reverse()
if forward == backward:
    print("It's a palindrome!")

else:
    print("It's not a palindrome :( You suck!")

print(forward)
print(backward)
