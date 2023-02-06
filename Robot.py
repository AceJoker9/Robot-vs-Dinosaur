#Creating commit to ensure we're doing this right 
from Weapon import Weapon
from Dinosaur import Dinosaur
class Robot(Dinosaur, Weapon): 
    def __init__(self, name, health, active_weapon):
        super(Dinosaur).__init__
        self.name = name 
        self.health = health
        self.active_weapon = active_weapon

#creating two objects one from each class. Dr.dealth is from Robot Class and  Iron hide is from dinosaur class
dr_dealth = Robot('smoke' , 1000, 500)
iron_hide = Dinosaur('iron_hide', 250, 1000) 



#creating a variable to use for a method to test code 


def testing_shot():
    x = dr_dealth.health 
    y = iron_hide.attack_power
    arrow_3 = x - y
    print(arrow_3)
    return(arrow_3)

testing_shot()
#Testing function returns the remaining health of the robot after taking a blow from ironhide.




def bull_shit(): 
    a = dr_dealth.active_weapon
    b = iron_hide.bar
    t_o = b - a
    print (t_o)
    return t_o


bull_shit()
# Thtat function returns the remaining health of iron hide after taking a blow from the robot


cherry = + int(50) 

new_health = cherry + bull_shit()

print(new_health) 

def crazy_attack():
    k = dr_dealth.active_weapon
    j = new_health
    last_breath = j - k
    print (last_breath)
    return last_breath

crazy_attack()









   
















 