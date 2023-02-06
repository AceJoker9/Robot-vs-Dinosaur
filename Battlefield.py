from Dinosaur import Dinosaur
from Robot import Robot

class Battlefield(Robot):
    def __init__(self):
        super()

     
#due to me already being slightly behind on assignments, What i will do is create everything from this file only. the methods from the other classes aren't being inheritent onto this file. Yes i can add the Class itself, but i cant access any methods. So all the methods and completion on this assignment will all be done on this one file.      
dr_guru = Robot('Dr.guru', 500, 300)
transfor_mer = Dinosaur('optimus',300,1000)



def run_game():

      display_welcome = "welcome to the match"
      print(display_welcome)

    
run_game()



def battle_phase(self):
        
        pass

def bumble_bee(): 
      x = transfor_mer.attack_power
      y = dr_guru.health
      robo_remain_health = y - x 
      print (robo_remain_health)
      return robo_remain_health

bumble_bee()

recap_1 = 'dr_guru health has dropped 300 points. dr.guru new health is 200'
print(recap_1) 

wire_cup = + int(250) 

robo_new_health = wire_cup + bumble_bee()
print(robo_new_health)



recap_2 = 'dr.guru has increased his new health by eating wire cups. Dr.guru new health is 450'
print(recap_2) 


def terminator_1(): 
      a = transfor_mer.bar
      b = dr_guru.attack_power
      damage = a - b
      print (damage)
      return damage


terminator_1()

recap_3 = 'Dr.guru pierced transfermer chest with his laser beam attack. Dropping his new health total down to 700'
print(recap_3)



recap_4 = 'Transformer is noticing that this robot has the capability to add more health, so he is deciding to end this battle quickly before it goes too far.'
print (recap_4) 

recap_5 = 'Transformer is going to hit the Robot with a double attack to end this battle swiftly'
print (recap_5)


def Optimus_2():
      c = robo_new_health
      d = transfor_mer.attack_power 
      finish_move = c - (d*2)
      print (finish_move)
      return finish_move

Optimus_2()

defeated = Optimus_2

recap_6 = 'the robot is deadly crushed by the transformer with the health total of -150'
print (recap_6)


def display_winner():
    winner = ('Transformer wins the battle by severly killing the robot, leaving his health at -150')
    print (winner)
    return winner


display_winner()

