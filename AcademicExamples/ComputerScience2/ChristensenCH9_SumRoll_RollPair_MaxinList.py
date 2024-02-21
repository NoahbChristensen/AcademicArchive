'''Dice Roll Program:
Given an object, GVDie, and an integer that represents the total sum desired
write a function roll_total() that displays the rolls it took to reach the desired total.'''

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
    main()