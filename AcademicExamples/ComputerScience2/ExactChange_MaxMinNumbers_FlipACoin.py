#23.5 Exact Change - Functions
'''
Define a function called exact_change that takes the total change amount in cents and calculates the change using the fewest coins.
The coin types are pennies, nickels, dimes, and quarters.
Then write a main program that reads the total change amount as an integer input, calls exact_change(),
and outputs the change, one coin type per line.
Use singular and plural coin names as appropriate, like 1 penny vs. 2 pennies. Output "no change" if the input is 0 or less.


def exact_change(total_change):
    if total_change <= 0:
        print("no change")
    else:
        dollar = total_change // 100
        total_change = total_change % 100
        quarter = total_change // 25
        total_change = total_change % 25
        dime = total_change // 10
        total_change = total_change % 10
        nickel = total_change // 5
        total_change = total_change % 5
        penny = total_change // 1
        total_change = total_change % 1
        if dollar > 1:
            print(dollar, "dollars")
        elif dollar == 1:
            print(dollar, "dollar")
        if quarter > 1:
            print(quarter, "quarters")
        elif quarter == 1:
            print(quarter, "quarter")
        if dime > 1:
            print(dime, "dimes")
        elif dime == 1:
            print(dime, "dime")
        if nickel > 1:
            print(nickel, "nickels")
        elif nickel == 1:
            print(nickel, "nickel")
        if penny > 1:
            print(penny, "pennies")
        elif penny == 1:
            print(penny, "penny")


def main():
    input_val = int(input("Enter the change amount in cents: "))
    exact_change(input_val)

if __name__ == "__main__":
    main()
'''

#23.11 LAB: Max and min numbers:
'''
Write a program whose inputs are four integers, and whose outputs are the maximum and the minimum of the four values.
The program must define and call the following two functions.
Define a function named max_number() that takes four integer parameters 
and returns an integer representing the maximum of the four integers.
Define a function named min_number() that takes four integer parameters 
and returns an integer representing the minimum of the four integers.
'''

def max_number(num1, num2, num3, num4):
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    if num4 > max_num:
        max_num = num4
    return max_num

def min_number(num1, num2, num3, num4):
    min_num = num1
    if num2 < min_num:
        min_num = num2
    if num3 < min_num:
        min_num = num3
    if num4 < min_num:
        min_num = num4
    return min_num

def main():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    num3 = int(input("Enter your third number: "))
    num4 = int(input("Enter your fourth number: "))
    print("max:", max_number(num1, num2, num3, num4))
    print("min:", min_number(num1, num2, num3, num4))

if __name__ == "__main__":
    main()







#23.12 LAB: Flip a coin:
'''
Define a function named coin_flip that returns "Heads" or "Tails" according to a random value 1 or 0.
Assume the value 1 represents "Heads" and 0 represents "Tails".
Then, write a main program that reads the desired number of coin flips as an input, calls function coin_flip() repeatedly
according to the number of coin flips, and outputs the results.
Assume the input is a value greater than 0.


import random

def coin_flip():
    if random.randint(0,1) == 0:
        return "Tails"
    else:
        return "Heads"
    
def main():
    result = coin_flip()
    print(result)

if __name__ == "__main__":
    main()
'''

