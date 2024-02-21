'''Dice Roll Program:
Given an object, GVDie, and an integer that represents the total sum desired
write a function roll_total() that displays the rolls it took to reach the desired total.

import random
import time

class GVDie:
    def __init__(self):
        self.my_value = random.randint(1, 6)
        self.rand = random.Random()
    
    def roll(self):
        self.my_value = self.rand.randint(1, 6)
        return self.my_value
    
    def set_seed(self, seed):
       self.rand.seed(seed)

    def compare_to(self, other):
        return self.my_value - other.my_value
    
    def roll_total(self, total):
        roll_count = 0
        roll_sum = 0
        while roll_sum < total:
            roll = self.roll()
            roll_sum += roll
            roll_count += 1
            print(f'Roll {roll_count}: {roll}\t||\tTotal: {roll_sum}')
            time.sleep(0.35)
        print(f'Total rolls: {roll_count}')
        return roll_count
    
def main():
    die = GVDie()
    die.set_seed(15)
    while True:
        total = int(input('Enter the total sum desired: '))
        die.roll_total(total)
        choice = input('Do you want to try another sum? (y/n): ')
        if choice.lower() != 'y':
            break

if __name__ == '__main__':
    main()'''

'''Roll Pair Program:
given two GVDie objects, and an integer that represents a desired value in the range of 1-6
we are looking to see how many rolls it takes to get a pair of the desired value.
Create a function roling_for_pair() that displays the rolls it took to reach the desired value.


import random
import time

class GVDie:
    def __init__(self):
        self.my_value = random.randint(1, 6)
        self.rand = random.Random()
    
    def roll(self):
        self.my_value = self.rand.randint(1, 6)
        return self.my_value
    
    def set_seed(self, seed):
       self.rand.seed(seed)

    def compare_to(self, other):
        return self.my_value - other.my_value
    
    def rolling_for_pair(self, desired):
        roll_count = 0
        while True:
            roll1 = self.roll()
            roll2 = self.roll()
            roll_count += 1
            print(f'Roll {roll_count}: {roll1}, {roll2}')
            if roll1 == desired and roll2 == desired:
                break
            time.sleep(0.35)
        print(f'Total rolls: {roll_count}')
        return roll_count
    
def main():
    die1 = GVDie()
    die2 = GVDie()
    die1.set_seed(15)
    die2.set_seed(15)
    while True:
        desired = int(input('Enter the desired value (1-6): '))
        die1.rolling_for_pair(desired)
        choice = input('Do you want to try another value? (y/n): ')
        if choice.lower() != 'y':
            break

if __name__ == '__main__':
    main()'''



''' Max Number in List program:

Write a program that takes a list of integers from from the user 
The program will display the list 
Then the Program will display the Highest Number, Lowest Number, Mean, Median, and Mode.

import statistics

def main():
    num_list = []
    while True:
        num = input('Enter a number (or "f" to finish): ')
        if num.lower() == 'f':
            break
        else:
            num_list.append(int(num))
    print(f'List: {num_list}')
    print(f'Highest Number: {max(num_list)}')
    print(f'Lowest Number: {min(num_list)}')
    print(f'Mean: {statistics.mean(num_list)}')
    print(f'Median: {statistics.median(num_list)}')
    print(f'Mode: {statistics.mode(num_list)}')

if __name__ == '__main__':
    main()'''



    
    