class Weapon: 
    def __init__(self, name, attack_power, active_weapon):
        self.name = name
        self.attack_power = 125
        self.active_weapon = 'blue'

gun_2 = Weapon('ak', 125, 'blue')      
print(gun_2.attack_power)

print(gun_2.active_weapon)



