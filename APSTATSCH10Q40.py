import random

def gen_component():
    return random.randint(0,9)

def gen_trial():
    total = 0
    for i in range(20):
        if(gen_component() == 0): # if a random integer 0-9 is 0, the total number of infringements in the trial is incremented
            total = total + 1
    return total

def gen_simulation():
    aboveFiveCount = 0
    trialCount = 10000
    for i in range(trialCount):
        result = gen_trial()
        if(result >= 5): # if the total infringements in the trial is 5 or greater the aboveFiveCount is incremented
            aboveFiveCount = aboveFiveCount + 1
            #print(result)
    probability = aboveFiveCount / trialCount
    print("Likelihood of seeing at least 5 out of 20 drivers using their phones illegally is " + str(probability) + "%")

gen_simulation()
