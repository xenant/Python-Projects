while True:
    askNum = input("Even or odd! Please input a number! ---> ")
    if askNum.isdigit():
        if int(askNum) % 4 == 0:
            print("the number you inputted is even! It's also divisible by 4, that's crazy!")
            print("You may input another number, or input a letter to stop the program")
        elif int(askNum) % 2 == 0:
            print("the number you inputted is even!")
            print("You may input another number, or input a letter to stop the program")
        else:
            print("the number you inputted is odd!")
            print("You may input another number, or input a letter/press enter to stop the program")
    else:
        break
