def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a)
    
def fibonacci_recursive(n, a=0, b=1):
    if n == 0:
        return
    print(a)
    fibonacci_recursive(n-1, b, a+b)

def main():
    UserOption = input("Which Fibonacci sequence would you like to generate? 1. Iterative 2. Recursive 3. Both: ")
    if UserOption == "1":
        n = int(input("Enter the number of terms you want in the Fibonacci sequence: "))
        print("Iterative Fibonacci sequence: ")
        fibonacci_iterative(n)
        goAgain = input("Would you like to generate another sequence? Y/N: ")
        if goAgain == "Y" or goAgain == "y":
            main()
        else:
            print("Goodbye!")
    elif UserOption == "2":
        n = int(input("Enter the number of terms you want in the Fibonacci sequence: "))
        print("Recursive Fibonacci sequence: ")
        fibonacci_recursive(n)
        goAgain = input("Would you like to generate another sequence? Y/N: ")
        if goAgain == "Y" or goAgain == "y":
            main()
        else:
            print("Goodbye!")
    elif UserOption == "3":
        n = int(input("Enter the number of terms you want in the Fibonacci sequence: "))
        print("Iterative Fibonacci sequence: \t| Recursive Fibonacci sequence:")
        for i in range(n):
            a_iterative, b_iterative = 0, 1
            a_recursive, b_recursive = 0, 1
            for j in range(i):
                a_iterative, b_iterative = b_iterative, a_iterative + b_iterative
                a_recursive, b_recursive = b_recursive, a_recursive + b_recursive
            print(f"{a_iterative}\t\t\t\t| {a_recursive}")
        goAgain = input("Would you like to generate another sequence? Y/N: ")
        if goAgain == "Y" or goAgain == "y":
            main()
        else:
            print("Goodbye!")
    else:
        print("Invalid input. Please try again.")
        main()

if __name__ == "__main__":
    main()