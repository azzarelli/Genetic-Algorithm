
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
    population.append(classes.PersonClass(i, random.randint(0,2),random.randint(0,4),random.randint(0,5)))

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

    #parents make children
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


while(len(alive) < 10000):

    alive = []
    
    # Determine who survives
    for obj in population:
        if(obj.surv >= 0.1): # harsh world only 40% of people live
            if(obj.age < 80): # kill people over the age ove 80
                alive.append(obj)
                beauty.append(obj.beauty)

    alive_num = len(alive)
        
    
    # Determine who has children && have them
    for i in range(0, alive_num):
        
        randNum = random.randint(0,10)
        
        for j in range(i+1, alive_num): # cycle through the population, look for compatible mates
            if((randNum == 1) and (beauty[i] == beauty[j])): # only 1/5 chance of having children
                                                            # but everyone mates with everyone at same beauty level
                if((alive[i].age > 25)and(alive[j].age>25)):
                    children_num = children_num + 1

                    child_intelligence = int((alive[i].intelligence + alive[j].intelligence)/2)
                    child_strength = int((alive[i].strength + alive[j].strength)/2)
           
                    alive.append(classes.PersonClass(children_num, beauty[i], child_intelligence, child_strength))


    population = alive
    track_size.append(len(alive))

    for obj in population:
        obj.age = obj.age + 1

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
