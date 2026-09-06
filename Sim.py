import random

# Contains the  stats of all the dogs 
class dog():
    #Stats
    def __init__(self, hp, atk):
        self.hp=hp
        self.atk=atk 
        self.win=0
        self.loss=0

    def attak(self):
            chance=random.randint(1,5)
            if chance <= 3:
                return self.atk
            else:
                return 0

    #Damage
    def damage(self,Eatk):
        self.hp-=Eatk
        if self.hp<=0:
            self.loss+=1
    #Healing after death
    def heal(self,hp):
        self.hp=hp

def alive_check():
    #Sees if any of the dogs are dead 
    if dog1.hp<=0: 
        dog1.heal(bace_hp)
        dog2.heal(bace_hp)
        dog2.win+=1
    elif dog2.hp<=0:
        dog1.heal(bace_hp)
        dog2.heal(bace_hp)
        dog1.win+=1
    else:  
        pass



bace_hp=20

dog1=dog(bace_hp,5)
dog2=dog(bace_hp,5)
turns=int(input("How many turn do you want to simulate- "))

for turn in range(0,turns):
    alive_check()   
    dog1.damage(dog2.attak())
    dog2.damage(dog1.attak())

print(f"Dog 1 - Wins: {dog1.win}, Losses: {dog1.loss}")
print(f"Dog 2 - Wins: {dog2.win}, Losses: {dog2.loss}")
