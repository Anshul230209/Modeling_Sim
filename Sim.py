import random

# Contains the  stats of all the dogs 
class dog():
    #Stats
    def __init__(self,legs,body,head):
        self.win=0
        self.loss=0
        #atk body parts 
        self.l_leg=legs
        self.r_leg=legs
        # def body parts
        self.body=body
        self.head=head
        #calc hp
        self.hp=(self.body+self.head+self.r_leg+self.l_leg)//2
        self.atk=(self.r_leg+self.l_leg)

    def attak(self):
            #Fahhhh IT is wrong remove
            atk_option=['l_leg','r_leg','body','head']
            if self.r_leg <=0:
                atk_option.pop('l_leg')
            if self.l_leg <=0:
                atk_option.pop('r_leg')
            if self.body <=0:
                atk_option.pop('body')            
            if self.head <=0:
                atk_option.pop('head')           

            chance=random.choice(atk_option)
            if chance =='l_leg':
                return self.atk, chance
            else:
                return 0

    #Damage
    def damage(self,Eatk,location):
        #use if statment to cheak location of atk
        self.hp-=Eatk
        if self.hp<=0:
            self.loss+=1
    #Healing after death
    def heal(self,legs,body,head):
        self.l_leg=legs
        self.r_leg=legs
        self.body=body
        self.head=head

def alive_check():
    #Sees if any of the dogs are dead 
    if dog1.hp<=0: 
        dog1.heal(bace_hp_legs,bace_hp_body,bace_hp_head)
        dog2.heal(bace_hp_legs,bace_hp_body,bace_hp_head)
        dog2.win+=1
    elif dog2.hp<=0:
        dog1.heal(bace_hp_legs,bace_hp_body,bace_hp_head)
        dog2.heal(bace_hp_legs,bace_hp_body,bace_hp_head)
        dog1.win+=1
    else:  
        pass



bace_hp_legs=10
bace_hp_body=20
bace_hp_head=15

dog1=dog(bace_hp_legs,bace_hp_body,bace_hp_head)
dog2=dog(bace_hp_legs,bace_hp_body,bace_hp_head)
turns=int(input("How many turn do you want to simulate- "))

for turn in range(0,turns):
    alive_check()   
    dog1.damage(dog2.attak())
    dog2.damage(dog1.attak())

print(f"Dog 1 - Wins: {dog1.win}, Losses: {dog1.loss}")
print(f"Dog 2 - Wins: {dog2.win}, Losses: {dog2.loss}")
