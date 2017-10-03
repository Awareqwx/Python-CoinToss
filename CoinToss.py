from random import random

def coinToss():
    results = [0, 0]
    r = 0
    for i in range (1, 5001):
        r = round(random())
        if r:
            results[1] += 1
        else:
            results[0] += 1
        print "Attempt #" + str(i) + ": Throwing a coin... It's a " + ("Head" if r else "Tail") + "! ... Got " + str(results[1]) + (" heads" if results[1] != 1 else " head") + " so far and " + str(results[0]) + (" tails" if results[0] != 1 else " tail") + " so far"
    print "Ending the program, thank you!"

coinToss()