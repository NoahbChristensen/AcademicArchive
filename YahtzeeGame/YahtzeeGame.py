import random
# from the central valley region of France, you might consider the fancier RanDome...
class Player:
    def __init__(self, name):
        self.name = name
        self.dice = [0, 0, 0, 0, 0]
        self.aces = 0
        self.twos = 0
        self.threes = 0
        self.fours = 0
        self.fives = 0
        self.sixes = 0
        self.three_of_a_kind = 0
        self.four_of_a_kind = 0
        self.full_house = 0
        self.small_straight = 0
        self.large_straight = 0
        self.yahtzee = 0
        self.chance = 0
        self.score = 0
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
    def calculateAces(self):
        return self.dice.count(1)
    def calculateTwos(self):
        return self.dice.count(2) * 2
    def calculateThrees(self):
        return self.dice.count(3) * 3
    def calculateFours(self):
        return self.dice.count(4) * 4
    def calculateFives(self):
        return self.dice.count(5) * 5
    def calculateSixes(self):
        return self.dice.count(6) * 6
    def calculateThreeOfAKind(self):
        for die in set(self.dice):
            if self.dice.count(die) >= 3:
                return sum(self.dice)
        return 0
    def calculateFourOfAKind(self):
        for die in set(self.dice):
            if self.dice.count(die) >= 4:
                return sum(self.dice)
        return 0
    def calculateFullHouse(self):
        counts = [self.dice.count(die) for die in set(self.dice)]
        if 2 in counts and 3 in counts:
            return 25
        else:
            return 0
    def calculateSmallStraight(self):
        sorted_dice = sorted(set(self.dice))
        if len(sorted_dice) >= 4 and any(sorted_dice[i] + 1 == sorted_dice[i+1] for i in range(len(sorted_dice)-1)):
            return 30
        else:
            return 0
    def calculateLargeStraight(self):
        sorted_dice = sorted(set(self.dice))
        if len(sorted_dice) == 5 and sorted_dice[-1] - sorted_dice[0] == 4:
            return 40
        else:
            return 0
    def calculateYahtzee(self):
        for die in set(self.dice):
            if self.dice.count(die) == 5:
                return 50
        return 0
    def calculateChance(self):
        return sum(self.dice)
    def scoreOption(self, userScoreOption):
        scoring_functions = {
            1: self.calculateAces,
            2: self.calculateTwos,
            3: self.calculateThrees,
            4: self.calculateFours,
            5: self.calculateFives,
            6: self.calculateSixes,
            7: self.calculateThreeOfAKind,
            8: self.calculateFourOfAKind,
            9: self.calculateFullHouse,
            10: self.calculateSmallStraight,
            11: self.calculateLargeStraight,
            12: self.calculateYahtzee,
            13: self.calculateChance
        }
        return scoring_functions.get(userScoreOption, lambda: "Invalid option")()
    def playerRound(self, round_number):
        if round_number == 1:
            self.rollDice(5)
            print(f"\n{self.name}'s initial roll is: {self.dice}")
        else:
            while True:
                reroll_option = input(f"\n{self.name} would you like to reroll? (y/n): ").lower()
                if reroll_option == "y":
                    dice_to_reroll = list(map(int, input("Enter the dice (1-5) to reroll (separate with spaces): ").split()))
                    self.rerollDice(dice_to_reroll)
                    print(f"\n{self.name}'s rerolled dice is: {self.dice}")
                    break
                elif reroll_option == "n":
                    print("Okay\n")
                    break
                else:
                    print("Invalid input, type 'y' or 'n'.")
        if round_number == 3:
            scoring_option = int(input(f"\n\nSCORING OPTIONS\n1: Aces = {self.aces}\n2: Twos = {self.twos}\n3: Threes = {self.threes}\n4: Fours = {self.fours}\n5: Fives = {self.fives}\n6: Sixes = {self.sixes}\n7: Three of a Kind = {self.three_of_a_kind}\n8: Four of a kind = {self.four_of_a_kind}\n9: Full House = {self.full_house}\n10: Small Straight (Sequence of 4 #) = {self.small_straight}\n11: Large Straight (Sequence of 5 #) = {self.large_straight}\n12:Yahtzee (Five of a Kind) = {self.yahtzee}\n13: Chance (Adding all Dice) = {self.chance}\nWhat would you like to score? (1-13): "))
            if 1 <= scoring_option <= 13:
                score = self.scoreOption(scoring_option)
                if isinstance(score, int):
                    self.score += score
                    print(f"\n{self.name}'s score is: {self.score}\n")
                else:
                    print(f"\n{self.name} cannot score that option, try again!\n")
def welcomeMessage():
    print("\n\nWelcome to Yahtzee!\nEach player will have 3 chances to roll the dice.\nThere are 13 different scoring options, which can only be selected once per game.\nThe player with the most points at the end of the game wins!\nGood luck!\n")
    scoringRules = input("Would you like to see the scoring options? (y/n): ").lower()
    if scoringRules == "y":
        print("\nThere are two sections for scoring, the Upper Section and the lower Section\n")
        print("The Upper Section is scored by adding the total of the dice with the same number.\n")
        print("The Lower Section is scored by the following options:\n")
        print("Three of a Kind: Add the total of all dice to calculate the score.")
        print("Four of a Kind: Add the total of all dice to calculate the score.")
        print("Full House: Score 25 points.")
        print("Small Straight: Score 30 points.")
        print("Large Straight: Score 40 points.")
        print("Yahtzee: Score 50 points.")
        print("Chance: Add the total of all dice to calculate the score.\n")
    else:
        print("Okay, let's play!\n")
def PlayerRound(round_number):
    num_players = int(input("How many players? "))
    players = []
    for _ in range(num_players):
        player_names = input("Player, what is your name? ")
        player = Player(player_names)
        players.append(player)
    game_over = False
    while not game_over:
        for round_number in range(1, 4):
            for player in players:
                player.playerRound(round_number)
        if round_number < 3:
                input("Press Enter to start the next player's turn...")
def main():
    welcomeMessage()
    PlayerRound(1)
if __name__ == "__main__":
    main()
