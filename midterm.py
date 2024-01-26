

import random
def task0():
    print("Melika Sherafat")
    print("email: melika.sherafatt@gmail.com")
    return
#--------------------------------------------------------------------------------------------------------

def task1():
    name = input("Your first name: ")
    last_name = input("Your last name: ")
    initial_fund = float(input("Initial funds to invest: "))
    annual_return = float(input("Annual return percentage: "))
    Year1 = initial_fund + (initial_fund * annual_return) /100
    Year2 = Year1 + (Year1 * annual_return) / 100
    Year3 = Year2 + (Year2 * annual_return) / 100
    Year4 = Year3 + (Year3 * annual_return) / 100
    Year5 = Year4 + (Year4 * annual_return) / 100
    print("Yearly return for", name[0].upper()+name[1:].lower(), last_name.upper())
    print("Initial deposit: "+ str(initial_fund)+"$")
    print("Year 1: ", round(Year1, 2))
    print("Year 2: ", round(Year2, 2))
    print("Year 3: ", round(Year3, 2))
    print("Year 4: ", round(Year4, 2))
    print("Year 5: ", round(Year5, 2))
    pass
#--------------------------------------------------------------------------------------------------------

def task2():
    curr = 0
    price = 1.0
    print("Soda Vending Machine")
    while curr < price:
        print("Current amount $" + str(curr), "out of $1.00")
        print(
            "Insert Coin\n1. Toonie ($2.00)\n2. Loonie ($1.00)\n3. Quarter ($0.25)\n4. Dime ($0.10)\n5. Nickel ($0.05)")
        selected = float(input("Selection [1-5]? "))

        if selected == 1:
            curr = curr + 2.0
        elif selected == 2:
            curr = curr + 1.0
        elif selected == 3:
            curr = curr + 0.25
        elif selected == 4:
            curr = curr + 0.10
        elif selected == 5:
            curr = curr + 0.05
        else:
            print("Invalid selection!")

    if curr == price:
        print("Total amount provided: $1.00")
        print("Thank you for your purchase.")

    elif curr > price:
        return_amount = round((curr - price), 2)
        print("Total amount provided: ", str(curr)+"$")
        print("Thank you for your purchase.")
        print("Please take your change", str(return_amount)+"$")
        pass
#--------------------------------------------------------------------------------------------------------

def task3():
    print("Rolling Dice 10 times")
    sum = 0
    range1 = range(1,11)
    num = 0
    for i in range1:
        dice = random.randint(1, 6)
        print("Roll"+str(i), "["+str(dice)+"]")
        sum = sum + dice


        if dice == 1:
            num += 1
    if num == 2:
        print("+10 Bonus for snake eyes [1][1]!")
        sum = sum + 10

    if sum > 35:
        print("Total", sum,"-- OVER 35 POINTS [YOU WIN!]")
    elif sum == 35:
        print("Total", sum,"-- Exactly 35 POINTS [YOU WIN!]")
    else:
        print("Total", sum,"-- TOO FEW POINTS [YOU LOSE!]")

    play_again = input("Enter 'Y' to play again: ")
    if play_again == "Y" or play_again == "y":
        task3()
    else:
        print("Thanks for playing\n GoodBye!")
        pass
#--------------------------------------------------------------------------------------------------------

def task4():
    str = input("Enter string with one word with ""quotes"": ")
    def countCases(str):
        Uppercase = 0
        Lowercase = 0
        for i in str:
            if i.isupper():
               Uppercase += 1
            elif i.islower():
                Lowercase += 1
            else:
                pass
        print("This string has", Uppercase, "uppercase characters.")
        print("This string has", Lowercase, "lowercase characters.")
    countCases(str)

    def flipCase(str):
        swapped_string = ""
        swapped_string += str.swapcase()
        print("Case flip: ", swapped_string)
    flipCase(str)

    def cutQuotedText(str):
        if str.count('"') == 2:
            L = str.index('"')
            R = str.rindex('"')
            removed = str[:L] + str[R+1:]
            print("Quote removed: ", removed)
        else:
            print("ERROR! No quoted text.")

    cutQuotedText(str)
    pass
#------------------------------------------------------------------------------------------------------------



# main function for EECS1015 midterm
def main():
    print("\n")
    task0()
    print("\n----------Task 1-----------")
    task1()
    print("\n----------Task 2-----------")
    task2()
    print("\n----------Task 3-----------")
    task3()
    print("\n----------Task 4-----------")
    task4()
    input("\nPress enter to exit.")

if __name__=="__main__":
    main()
