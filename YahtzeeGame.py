import random

''' YAHTZEE GAME
There needs to be 5 dice
There needs to be a way to reroll specific dice
There needs to be a way to score the dice
There needs to be a way to keep score
There needs to be three rolls per turn
'''


class Player:
    def __init__(self, name):
        self.name = name
        self.dice = [0, 0, 0, 0, 0]
        self.score = 0

    def namePlayer(self):
        self.name = input("What is your name? ")

    def rollDice(self, numDice):
        self.dice = [random.randint(1, 6) for _ in range(numDice)]
        return self.dice
    
    def rerollDice(self, dice_to_reroll):
        for i in dice_to_reroll:
            if 1 <= i <= 5:
                self.dice[i - 1] = random.randint(1, 6)
            else:
                print(f"Invalid input: {i}. Enter the dice (1-5) to reroll (separate with spaces)")
        return self.dice
    
    def curDice(self):
        print(f"{self.name}'s dice are: {self.dice}")

    def calculateAces(self):
        print("Calculating Aces")

    def calculateTwos(self):
        print("Calculating Twos")
    
    def calculateThrees(self):
        print("Calculating Threes")
    
    def calculateFours(self):
        print("Calculating Fours")
    
    def calculateFives(self):
        print("Calculating Fives")
    
    def calculateSixes(self):
        print("Calculating Sixes")    
    
    def calculateThreeOfAKind(self):
        count = [0] * 6
        for die in self.dice:
            count[die - 1] += 1

        for i in range(6):
            if count[i] >= 3:
                return sum(self.dice)
        return 0
    
    def calculateFourOfAKind(self):
        print("Calculating Four of a Kind")
    
    def calculateFullHouse(self):
        print("Calculating Full House")
    
    def calculateSmallStraight(self):
        print("Calculating Small Straight")
    
    def calculateLargeStraight(self):
        print("Calculating Large Straight")
    
    def calculateYahtzee(self):
        print("Calculating Yahtzee")
    
    def calculateChance(self):
        print("Calculating Chance")
    
    def scoreOption(self, userScoreOption):
        if userScoreOption == 1:
            return self.calculateAces()
        elif userScoreOption == 2:
            return self.calculateTwos()
        elif userScoreOption == 3:
            return self.calculateThrees()
        elif userScoreOption == 4:
            return self.calculateFours()
        elif userScoreOption == 5:
            return self.calculateFives()
        elif userScoreOption == 6:
            return self.calculateSixes()
        if userScoreOption == 7:  
            return self.calculateThreeOfAKind()
        elif userScoreOption == 8:
            return self.calculateFourOfAKind()
        elif userScoreOption == 9:
            return self.calculateFullHouse()
        elif userScoreOption == 10:
            return self.calculateSmallStraight()
        elif userScoreOption == 11:
            return self.calculateLargeStraight()
        elif userScoreOption == 12:
            return self.calculateYahtzee()
        elif userScoreOption == 13:
            return self.calculateChance()





    def playerRound(self, round_number):
        if round_number == 1:
            self.rollDice(5)
            print(f"{self.name}'s initial roll is: {self.dice}")
        else:
            while True:
                reroll_option = input("Would you like to reroll? (y/n): ").lower()
                if reroll_option == "y":
                    dice_to_reroll = list(map(int, input("Enter the dice (1-5) to reroll (separate with spaces): ").split()))
                    self.rerollDice(dice_to_reroll)
                    print(f"{self.name}'s rerolled dice is: {self.dice}")
                    break
                elif reroll_option == "n":
                    print("Okay")
                    break
                else:
                    print("Invalid input, type 'y' or 'n'.")
        if round_number == 3:

            scoring_option = int(input("\n\nSCORING OPTIONS\n1: Aces\n2: Twos\n3: Threes\n4: Fours\n5: Fives\n6: Sixes\n7: Three of a Kind\n8: Four of a kind\n9: Full House\n10: Small Straight (Sequence of 4 #)\n11: Large Straight (Sequence of 5 #)\n12:Yahtzee (Five of a Kind)\n13: Chance (Adding all Dice)\nWhat would you like to score? (1-13): "))
            if 1 <= scoring_option <= 13:
                score = self.scoreOption(scoring_option)
                if score > 0:
                    self.score += score
                    print(f"{self.name}'s score is: {self.score}")
                else:
                    print(f"{self.name} cannot score that option, try again!")


    def curDice(self):
        print(f"{self.name}'s dice are: {self.dice}")



def welcomeMessage():
    print("Welcome to Yahtzee!\nEach player will have 3 rounds to roll the dice and score points.\nThere are 13 different scoring options, which can only be selected once per game\nThe player with the most points at the end of the game wins!\nGood luck!")
    scoringRules = input("Would you like to see the scoring options? (y/n): ").lower()

    if scoringRules == "y":
        print("\nThere are two sections for scoring, the Upper Section and the lower Section\n")
        print("The Upper Section is scored by adding the total of the dice with the same number")
        print("The Lower Section is scored by the following options:")
        print("Three of a Kind: Add the total of all dice to calculate the score.")
        print("Four of a Kind: Add the total of all dice to calculate the score.")
        print("Full House: Score 25 points.")
        print("Small Straight: Score 30 points.")
        print("Large Straight: Score 40 points.")
        print("Yahtzee: Score 50 points.")
        print("Chance: Add the total of all dice to calculate the score.")
    else:
        print("Okay, let's play!")



def main():
    welcomeMessage()
    num_players = int(input("How many players (1-4)? "))
    players = []
    for i in range(num_players):
        player = Player("")
        player.namePlayer()
        players.append(player)

    for player in players:
        for round_number in range(1, 4):
            player.playerRound(round_number)

if __name__ == "__main__":
    main()