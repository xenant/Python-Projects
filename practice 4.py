"Create a program that asks the user for a number and then prints out a list of all the divisors of that number."
"(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)"

num = int(input("Please input a number and we'll print out a list of all the divisors for that number  -->  "))

init_list = range(1,(num+1))
final_list = [] 
for i in init_list:
    if num % i == 0:
        final_list.append(i)

print(final_list)
