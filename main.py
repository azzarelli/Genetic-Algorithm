
# This Genetic algorythm focuses on the more realistic evolution methods that exist - based around three qualities 'Beauty', 'Intelligence', 'Strength'
    # Beauty determines who has sex with who. As with most species attraction dictates who can mate.
        # For the moment only people of the same beauty will mate
    # Strength is a the main contributor to survival - the stronger you are the higher your survival rating is (".surv")
    # Intelligence is a large contributor to survival also - the smarter people have higher survival raiting

    # Survival rating (/11) = Beauty (2) + Strength (5) + Intelligence(4)


import classes
import random
from datetime import datetime

import plotly.graph_objects as go


# Generate first population (All is random)
# Qualitites: strength (5), beauty(2), intelligence(4),
#   returns fitness
# Changes: Mutation and Parent Cross Over


track_size = []
track_beauty = []
track_strength = []
track_intelligence = []

population = []
random.seed(datetime.now())
alive = []
beauty = []

for i in range(100):
    population.append(classes.PersonClass(i, random.randint(0,2),random.randint(0,8),random.randint(0,10)))

alive_num = len(population)

alive = []
beauty = []

    # who survives in population
for obj in population:
    if(obj.surv >= 0.6): # harsh world only 40% of people live
        if(obj.age < 3):
            alive.append(obj)
            beauty.append(obj.beauty)

alive_num = len(alive)

children_num = 0

#   parents make children
for i in range(0, alive_num):
    randNum = random.randint(0,5)
    for j in range(i+1, alive_num):
        if((randNum == 1) and (beauty[i] == beauty[j])): # only 1/5 chance of having children
                                                            # but everyone mates with everyone at same beauty level
            children_num = children_num + 1

            child_intelligence = int((alive[i].intelligence + alive[j].intelligence)/2)
            child_strength = int((alive[i].strength + alive[j].strength)/2)
           
            alive.append(classes.PersonClass(children_num, beauty[i], child_intelligence, child_strength))
            

track_size.append(len(alive))

# Initial Tracking Values
num_str = 0
num_intel = 0
num_beau = 0

    
for obj in population:
    if(obj.beauty == 2):
        num_beau = num_beau + 1
    if(obj.strength == 5):
        num_str = num_str + 1
    if(obj.intelligence == 4):
        num_intel = num_intel + 1

    
track_intelligence.append(num_intel)
track_strength.append(num_str)
track_beauty.append(num_beau)


while(len(alive) < 1000):

    # Generate Random Constants to be used
    randNum1 = random.random() # number from 0.0 to 1.0, used for twin, triplet, quadruplet chance ... 
    randNum2 = random.randint(0,2) # number between 0 and 2, set threshold for death due to stupidity
    
    alive = []
    
    # Determine who survives
    for obj in population:
        if(obj.surv >= 0.1): # harsh world only 90% of people live
            if(obj.intelligence > randNum2):
                if(obj.age < random.randint(75,100)): # people between ages of 75 and 100 are more likely to die
                                                    # thos younger than these random ages are passed on
                    alive.append(obj)
                    beauty.append(obj.beauty)

    alive_num = len(alive)

    # Determine who has children && have them
    for i in range(0, alive_num):
        
        randNum = random.randint(0,10)
        for j in range(i+1, alive_num): # cycle through the population, look for compatible mates
            if((randNum == 1) and (beauty[i] == beauty[j])): # but everyone mates with everyone at same beauty level

                if((alive[i].age > 25)and(alive[j].age>25)and(alive[i].age<55)and(alive[j].age<55)): # age of reproduction becomes a factor

                    if((alive[i].mated == 0)and(alive[j].mated == 0)): # only mates with someone once a year
                        child_intelligence = int((alive[i].intelligence + alive[j].intelligence)/2)
                        child_strength = int((alive[i].strength + alive[j].strength)/2)

                        # Likelihood of having more than one child at once
                        if(randNum1 < 0.004): # 0.40% of having twins
                            alive.append(classes.PersonClass(children_num, beauty[i], child_intelligence, child_strength))
                            alive.append(classes.PersonClass(children_num+1, beauty[i], child_intelligence, child_strength))
                            children_num = children_num + 2
                        elif(randNum1 < 0.00412): # 0.012% of having triplets
                            alive.append(classes.PersonClass(children_num, beauty[i], child_intelligence, child_strength))
                            alive.append(classes.PersonClass(children_num+1, beauty[i], child_intelligence, child_strength))
                            alive.append(classes.PersonClass(children_num+2, beauty[i], child_intelligence, child_strength))
                            children_num = children_num + 3
                        else: # Otherwise have my own
                            alive.append(classes.PersonClass(children_num, beauty[i], child_intelligence, child_strength))
                            children_num = children_num + 1
                        
                        alive[i].mated = alive[i].mated + 1
                        alive[j].mated = alive[j].mated + 1


    population = alive
    track_size.append(len(alive))

    # age everyone and return mated count to 0
    for obj in population:
        obj.age = obj.age + 1
        obj.mated = 0

    # Calculate Tracking Values
    num_str = 0
    num_intel = 0
    num_beau = 0

    
    for obj in population:
        if(obj.beauty == 2):
            num_beau = num_beau + 1
        if(obj.strength == 5):
            num_str = num_str + 1
        if(obj.intelligence == 4):
            num_intel = num_intel + 1

    
    track_intelligence.append(num_intel)
    track_strength.append(num_str)
    track_beauty.append(num_beau)

    beauty = []


step = []

for i in range(len(track_size)):
    print(track_size[i], ' ', track_beauty[i], ' ', track_intelligence[i], ' ', track_strength[i])

    step.append(i)


# Graphing Outcome

fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=step, y=track_size,
                    mode='lines+markers',
                    name='Population Size'))

fig.add_trace(go.Scatter(x=step, y=track_beauty,
                    mode='lines+markers',
                    name='# of Most Beautiful'))
fig.add_trace(go.Scatter(x=step, y=track_intelligence,
                    mode='lines',
                    name='# of Most Intelligent'))
fig.add_trace(go.Scatter(x=step, y=track_strength,
                    mode='lines',
                    name='# of Most Strength'))

fig.show()
