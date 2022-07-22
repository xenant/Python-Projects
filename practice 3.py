# write a program that prints out all the elements of the list that are less than 5.

init_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
final_list = [] 

num = int(input("Please input a number, and the program will print out the numbers in the list smaller than the given number -->   "))
for i in init_list:
    if i < num:
        final_list.append(i)
    elif i <= init_list[0]:
        print("lol no numbers in this list would satisfy ;)")
        break

if len(final_list) > 0:
    print(final_list)