Class: GameOperator
    Responsibilities:
    Randomly choose first player
    Add sum of scores for each turn
    Declare Winner at 100 pts/End Game

    Collaborators:
    Player/Turn/Dice


Class: UserPlay
    Responsibilities:
        Person(responsibilities):
        decide whether to hold or roll
        Computer(responsibilities):
        roll until 1 or >= 20
    
    Collaborators:
    GameOperator/Dice/Turn

Class:  ComputerPlay
    Responsibilities:
        Continue rolls until score for that turn >= 20
    Collaborators:
    GameOperator/Dice/Turn

Class: Dice
    Responsibilities:
    Randomly choose number between 1 and 6 to assign value to roll
    
    Collaborators:
    Player/Turn/GameOperator


Class: Turn
    Responsibilites:
    Sum values of individual die roll each turn
        If "1", go to next player
        If "hold", go to next player
    
    Collaborators:
    Dice/Player/GameOperator
