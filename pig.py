import random

class Dice:

    def __init__(self, sides = 6):
        self.sides = sides
        self.roll = roll

    def roll(self):
        return random.randint(1, self.sides)
        print("Your score was: " + roll)


class UserPlay:

    def __init__(self, person):
        self.person = person
        self.score = score
        self.roll = roll
    # def person_choice(self):
    
    def player_turn(self):
        roll()
        return turn_score(self, person)
        if roll ==  1:
            print("You rolled a Pig!")
            switch_turn()
        if roll != 1:
            print("Your score so far is: " self.turn_score.person)
            turn_choice()
        while turn_choice == True:
            roll()
        print("Your score overall is: " self.running_score.person)
        switch_turn()
    
    def person_turn_score(self):
        return self.running_score + turn_score(person)
        print("Your score this turn is: " self.person_turn_score)


class ComputerPlay:

    def __init__(self, computer):
        self.computer = computer
        self.score = score
        self.roll = roll

    def computer_choice(self):
        roll()
        if roll == 1:
            print("The computer's overall score is: " running_score.computer)
            switch_turn()
        return turn_score(self, computer)
            if turn_score < 20:
                roll()
            return self.computer_turn_score
            print("The computer's overall score is: " running_score.computer)
            switch_turn()
    
    def computer_turn_score(self):
        return self.running_score + turn.score(computer)
        print("The computer's score this turn is: " self.computer_turn_score)

class Turn:

    def __init__(self, turn):
        self.turn = turn
        self.roll = roll

    def switch_turn(self):
        turn_choice() == false

    def turn_choice(self):
        input("Would you like to roll again (y)es or (n)o? ")
        if input.lower() is not "yes" or "y":
            switch_turn()
            if input.lower() is "yes" or "y":
                turn_choice() == true
    
    def turn_score(self, person, computer):
        total = sum([roll() for roll in self.roll])
        return total
        print(total)

class GameOperator:

    def __init__(self, operate):
        self.operate = operate
        self.Dice = Dice
        self.score = score
        self.roll = roll
    
    def first_turn(self):
        roll()
        if self.Dice.roll() > self.dice.roll:
            print("You have the first turn!")
            return turn_choice(self, person)
        # print("The computer has the first turn!")
        # return turn_choice(self, computer)
        """ Took the above two lines out to ensure player.person goes first"""
    
    def running_score(self, player):
        self.score.person += turn_score.person
        self.score.computer += turn_score.computer

    def end_game(self, player):
        if self.running_score.person >= 100:
            print("You won this game of Pig!")
            break
        if self.running_score.computer >= 100:
            print("The computer beat you this time!")
            break

def run_game():
    roll()
    first_turn()
run_game()



    
    






    