#Creating commit to ensure we're doing this right 
from Weapon import Weapon
from Dinosaur import Dinosaur
class Robot(Dinosaur, Weapon): 
    def __init__(self, name, health, active_weapon):
        super(Dinosaur).__init__
        self.name = name 
        self.health = 1000
        self.active_weapon = 300

#creating two objects one from each class. Dr.dealth is from Robot Class and  Iron hide is from dinosaur class
dr_dealth = Robot('smoke',450,'blue')
iron_hide = Dinosaur('iron_hide', 250, 1000) 



#creating a variable to use for a method to test code 
arrow_2 = dr_dealth.health - iron_hide.attack_power

def testing_shot():
    arrow_2 = dr_dealth.health - iron_hide.attack_power
    print(arrow_2)
    return(arrow_2)



#Creating variable to test method 
slash = iron_hide.bar - dr_dealth.active_weapon


def shits_giggles():
   slash = iron_hide.bar - dr_dealth.active_weapon
   dino_newbar = slash
   print(dino_newbar)
   return(dino_newbar)




   
















 