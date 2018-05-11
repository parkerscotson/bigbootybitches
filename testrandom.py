import random
#!/usr/bin/python
from datetime import datetime

def randomNumber():
    random.seed(datetime.now())
    return random.randint(1,80)

def getKenoNumbers():

    output = []
    for i in range (0,20):
        output.append(randomNumber())
    return output

def getUserSelection():
    amount = input("how many numbers do want to pick? (2-10)")

    if not amount.isdigit():
        print ("you really fucked up")
    if int(amount) <=1 or int(amount) >=11:
        print("out of bounds")
    output = []
    while True:
        choice = input("Choose a number between 1 and 80:")
        if not choice.isdigit():
            print ("that aint no number fool")
        if int(choice) <=0 or int(choice) >=81:
            print ("up to 80 boiiii")
        output.append(int(choice))
        if len(output) == int(amount):
            break
    return output
def compareChoices(user, machine):
    output = []
    matched = 0
    matchedNumbers = []
    for item in user:
        if item in machine:
            matched +=1
            matchedNumbers.append(item)
    output.append(matched)
    output.append(matchedNumbers)
    return output
userChoices = getUserSelection()
kenoNumbers = getKenoNumbers()

#####DEBUddd
kenoNumbers[0] = 1
kenoNumbers[1] = 2
kenoNumbers[2] = 3
#####

results = compareChoices(userChoices, kenoNumbers)

print ("User chose: {}".format(userChoices))
print ("Machine chose: {}".format(kenoNumbers))
print ("User matched: {} draws, and matched these number: {}".format(results[0], results[1]))
