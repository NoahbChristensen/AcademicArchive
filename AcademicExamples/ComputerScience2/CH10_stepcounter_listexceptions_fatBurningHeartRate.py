def steps_to_miles(steps):
    if steps < 0:
        raise ValueError("Exception: Negative step count entered.")
    return steps / 2000

def list_exceptions():
    names = ["John", "Doe", "Jane", "Smith", "Tom", "Brown", "Alice", "Miller", "Bob", "Johnson"]
    try:
        index = int(input("Enter an index: "))
        print(names[index])
    except IndexError as e:
        if index < 0:
            print("Exception! Negative index entered.")
            print(names[0])
        else:
            print("Exception! Positive index entered.")
            print(names[-1])

def fat_burning_heart_rate(age):
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")
    return 0.7 * (220 - age)

def get_age():
    age = int(input("Enter your age: "))
    return age

def main():
    while True:
        print("\n\n1. Calculate step count")
        print("2. List exceptions")
        print("3. Calculate fat burning heart rate")
        print("4. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            try:
                steps = int(input("Enter the number of steps: "))
                print(steps_to_miles(steps))
            except ValueError as e:
                print(e)
        elif choice == 2:
            list_exceptions()
        elif choice == 3:
            try:
                age = get_age()
                print(fat_burning_heart_rate(age))
            except ValueError as e:
                print(e)
                print("Could not calculate heart rate info.")
        elif choice == 4:
            break

if __name__ == "__main__":
    main()