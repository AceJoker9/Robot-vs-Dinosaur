from Dinosaur import Dinosaur
from Robot import Robot

class Battlefield(Robot):
    def __init__(self):
        super()

     
#due to me already being slightly behind on assignments, What i will do is create everything from this file only. the methods from the other classes aren't being inheritent onto this file. Yes i can add the Class itself, but i cant access any methods. So all the methods and completion on this assignment will all be done on this one file.      
dr_guru = Robot('guru', 500, 'laserbeam')
transfor_mer = Dinosaur('optimus',300,1000)

#creating the first method/variable for the battle
first_attack = transfor_mer.bar - dr_guru.active_weapon
t_newhealth = first_attack


def bullshit(x,y):
      x = transfor_mer.attack_power
      y = dr_guru.health
      bout_time = x - y
      print(bout_time)
      return bout_time 




bullshit()


def initial_attackt():
      first_attack = transfor_mer.bar - dr_guru.active_weapon
      t_newhealth = first_attack
      print(t_newhealth)

      return t_newhealth

def second_attack():
      bonus = t_newhealth + int(450)
      print (bonus)
      return bonus


initial_attack()





second_attack()

def bumblebee():
     damage = int((dr_guru.health) - int(transfor_mer.attack_power) * 2)
     print(damage)
     return damage



bumblebee()




def run_game():


        

    display_welcome = "welcome to the match"


    print(display_welcome)

    



def battle_phase(self):
        
        pass

def display_winner(self):
        
        pass

