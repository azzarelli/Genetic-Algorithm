import random

def fitness(b, s, i):
    return b+s+i

def survival(fit):
    return float(fit/11)
        
class PersonClass(object):

# Constructor
    def __init__(self, number, beauty, intelligence, strength):
        self.beauty = beauty
        self.intelligence = intelligence
        self.strength = strength
        self.fit = strength + beauty + intelligence
        self.surv = float(self.fit/11)
        self.id = number
        self.age = 0

# Deterministic  
    mutation_choice = random.random() # returns num from 0 to 1
   
    def determine_mutation():
        if(mutation_choice < 0.7): # 60% chance for no mutation
            mutation_choice = 0
        elif(mutation_choice < 0.75): # 5% chance for beauty to change
            beauty = random.randint(0,2) # mutations are random
        elif(mutation_choice < 0.85): # 10% chance for intelligence mutation
            intelligence = random.randint(0,4)
        elif(mutation_choice <= 1): # 15% chance for strength change
            strength = rand.randint(0,5)
            
