#Creating commit to ensure we're doing this right 
from Weapon import Weapon
class Robot: 
    def __init__(self, name):
        self.name = name 
        self.health = 1000
        self.active_weapon = Weapon("laser beam", 50)
        
    def attack(self, dinosaur):
        pass

