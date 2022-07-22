# write a program that returns a list that contains only the elements that are common between the lists
#  (without duplicates). Make sure your program works on two lists of different sizes.
import random 
range_one = int(input("Please input the length of the first list --> "))
range_two = int(input("Please input the length of the second list --> "))

first = random.sample(range(1, 100), range_one)
second =  random.sample(range(1, 100), range_two)
final = [] 



if len(first) > len(second):
    for i in second:
        if i in first:
            final.append(i)
else:
    for i in first:
        if i in second:
            final.append(i)

print("below is the first list")
print(first)
print("------------------------------------")
print("below is the second list")
print(second)
print("------------------------------------")
print("below is the actual output:")
print(final)