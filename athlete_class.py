import random
import time

class Athlete():
    
    name = ''
    hp = 100
    
    def __init__(self, name):
        self.name = name
        print('Fighter selected, his name is', name)
    
    time.sleep(1)
    
    def kick(self, other):
        print(self.name, 'hits', other.name)
        other.hp -= 20
    
    time.sleep(1)    
       
fighter1 = Athlete('Sanya')
time.sleep(1)
fighter2 = Athlete('Danya')

time.sleep(1)

print()
print(fighter1.name,'has', fighter1.hp, 'HP')
time.sleep(1)
print(fighter2.name,'has', fighter2.hp, 'HP')
print()

time.sleep(1)

print('Fight!!!')
print()

time.sleep(1)


while fighter1.hp and fighter2.hp > 0:
        
        fighters = 1,2
        hit = random.choice(fighters)
    
        if hit == 1:
            fighter1.kick(fighter2)
            print(fighter2.name,'has', fighter2.hp, 'HP')
            print()
            
            time.sleep(1)
    
        elif hit == 2:
            fighter2.kick(fighter1)
            print(fighter1.name,'has', fighter1.hp, 'HP')
            print()
            
            time.sleep(1)            
        
        if fighter1.hp == 0:
            print(fighter2.name, 'wins!')
            
        elif fighter2.hp == 0:
            print(fighter1.name, 'wins!')
            
            time.sleep(1)
            
        if fighter1.hp == 100 and fighter2.hp == 0:
            print()
            print('Flawless victory!')
        
        elif fighter1.hp == 0 and fighter2.hp == 100:
            print()
            print('Flawless victory!')

time.sleep(1)    

print()
print('Fight is over!')