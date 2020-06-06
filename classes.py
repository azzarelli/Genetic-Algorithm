import random
from datetime import datetime

class PersonClass(object):
    random.seed(datetime.now())
    
# Constructor
    def __init__(self, number, beauty, intelligence, strength): 
        randNum = random.random()
        
        if(randNum < 0.01): #   1% Genetic Mutation 
            if(randNum < 0.002):
                self.beauty = (beauty + random.randint(0,10))%2
                self.intelligence = intelligence
                self.strength = strength
            elif(randNum < 0.006):
                self.intelligence = (intelligence + random.randint(0,10))%2
                self.beauty = beauty
                self.strength = strength
            else:
                self.strength = (strength + random.randint(0,10))%2
                self.beauty = beauty
                self.intelligence = intelligence
        else:
            self.beauty = beauty
            self.intelligence = intelligence
            self.strength = strength

        self.fit = strength + beauty + intelligence
        self.surv = float(self.fit/20)
        self.id = number
        self.age = 0
        self.mated = 0
