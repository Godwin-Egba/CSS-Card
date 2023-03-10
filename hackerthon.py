
import random
import time

estimatedPopulation = 552725

#function that generate random int
#bracket is the range
#random library

while True:
    death_rate = random.randint(0,10)
    birthRate = random.randint(0, 30)
    populationTravelingOut = random.randint(0,60)
    populationTravelingIn = random.randint(0,100)
    farterlity = death_rate + populationTravelingOut
    mortality = birthRate + populationTravelingIn
    currentPopulation = mortality + (estimatedPopulation - farterlity)
    print ("there are " + str(death_rate) + " death")
    print ("there are " + str(birthRate) + " birth")
    print ("there are " + str(populationTravelingIn) + " travelingIn")
    print ("there are " + str(populationTravelingOut)+ " travelingOut")
    time.sleep(30)
    
    #time is used for sleep
    
    