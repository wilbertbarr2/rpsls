#1 should i import the rules or should i leave it out from rules import Rules

from rules import Rules


from gestures import Gestures


from random import random


#2 how do i get chose a gesture to pick a gesture
#3 Do i Need to add a couple more var to player class
class Player:
    def __init__(self):
        self.human = (input())
        self.chose_a_Gesture =

        pass

#4 how do i get the gesture to be automatically picked(making a rand chose generator
#(4) with import random then trying to printing thr results


#5 need to know if this is how you put inheritance together

class Human2(Player):
    def __init__(self):
        super.__init__()


#6 wanting to inherit gestures to Ai
#7 im trying to figure out how do i inherit player 1 info to ai info

class AI :
    def __init__(self):
        def auto_gesture(self):
            self.gestures = [Gestures("rock"), Gestures("paper"), Gestures("scissors"), Gestures("lizard"),
                             Gestures("spock")]
            self.random = (random.choices())
            print(self.random)

    def __int__(self):
        len(self.Gesture.)
        print(self.gestures)




