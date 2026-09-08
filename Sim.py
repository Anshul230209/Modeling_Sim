import random

# Contains the stats of all the monsters 
class Monster:
###################################################################
    # Stats
    def __init__(self, legs, body, head):
        self.win = 0
        self.loss = 0
        self.draw = 0
        # def body parts
        self.l_leg = legs
        self.r_leg = legs
        self.body = body
        self.head = head
        # calc hp and atk
        self.hp = (self.body + self.head + self.r_leg + self.l_leg) // 2
        self.atk = (self.r_leg + self.l_leg)

####################################################################
    def get_atk_options(self):
        options = []
        if self.l_leg > 0:
            options.append('l_leg')
        if self.r_leg > 0:
            options.append('r_leg')
        if self.body > 0:
            options.append('body')            
        if self.head > 0:
            options.append('head')
        
        # Fallback in case all parts reach 0 but HP is somehow still > 0
        return options if options else ['body']

####################################################################
    def attack(self, options):          
        chance = random.choice(options)
        # Roll for damage instead of using a static number
        actual_damage = random.randint(1, self.atk)
        return actual_damage, chance

####################################################################
    # Damage
    def damage(self, Eatk, location):
        self.hp -= Eatk
        if self.hp <= 0:
             self.loss += 1
        elif location == 'l_leg':
             self.l_leg -= Eatk
        elif location == 'r_leg':
             self.r_leg -= Eatk
        elif location == 'body':
             self.body -= Eatk
        elif location == 'head':
             self.head -= Eatk # Fixed: was previously reducing l_leg instead of head

####################################################################
    # Healing after death
    def heal(self, legs, body, head):
        self.l_leg = legs
        self.r_leg = legs
        self.body = body
        self.head = head
        # Fixed: HP and ATK must be recalculated upon healing
        self.hp = (self.body + self.head + self.r_leg + self.l_leg) // 2
        self.atk = (self.r_leg + self.l_leg)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
def alive_check():
    # Check for a tie (both die on the same turn) first
    if monster1.hp <= 0 and monster2.hp <= 0:
        monster1.heal(base_hp_legs, base_hp_body, base_hp_head)
        monster2.heal(base_hp_legs, base_hp_body, base_hp_head)
        monster1.draw += 1
        monster2.draw += 1
        # Optional: Add a draw counter here if you want to track them
    elif monster1.hp <= 0: 
        monster1.heal(base_hp_legs, base_hp_body, base_hp_head)
        monster2.heal(base_hp_legs, base_hp_body, base_hp_head)
        monster2.win += 1
    elif monster2.hp <= 0:
        monster1.heal(base_hp_legs, base_hp_body, base_hp_head)
        monster2.heal(base_hp_legs, base_hp_body, base_hp_head)
        monster1.win += 1

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#

base_hp_legs = 10
base_hp_body = 20
base_hp_head = 15

monster1 = Monster(base_hp_legs, base_hp_body, base_hp_head)
monster2 = Monster(base_hp_legs, base_hp_body, base_hp_head)

turns = int(input("How many turns do you want to simulate? "))

for turn in range(turns):
    # 50% chance for Monster 1 to strike first
    if random.choice([True, False]):
        monster2.damage(*monster1.attack(monster2.get_atk_options()))
        if monster2.hp > 0: # M2 only attacks back if it survived M1's hit
            monster1.damage(*monster2.attack(monster1.get_atk_options()))
    else:
        monster1.damage(*monster2.attack(monster1.get_atk_options()))
        if monster1.hp > 0:
            monster2.damage(*monster1.attack(monster2.get_atk_options()))
            
    alive_check()
    

print(f"Monster 1 - Wins: {monster1.win}, Losses: {monster1.loss}")
print(f"Monster 2 - Wins: {monster2.win}, Losses: {monster2.loss}")