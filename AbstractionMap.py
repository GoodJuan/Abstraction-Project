global distances
distances = []

class city:
    xCor = 0
    yCor = 0
    name = ""
    connectedCities = []

    def __init__(self, x, y, name):
        self.xCor = x
        self.yCor = y
        self.name = name
    def addCities(self, newCities):
        self.connectedCities = self.connectedCities + newCities

    def getCities(self):
        return self.connectedCities
    def getX(self):
        return self.xCor
    def getY(self):
        return self.yCor
    def getName(self):
        return self.name

cityA = city(0,0,"A")
cityB = city(200,200,"B")
cityC = city(60, 20,"C")
cityD = city(20,170,"D")
cityE = city(30,90,"E")
cityF = city(185, 160,"F")

#Telling the computer which cities connect to which
cityA.addCities([cityE, cityD, cityC])
cityB.addCities([cityC, cityF])
cityC.addCities([cityA, cityF, cityB])
cityD.addCities([cityF, cityA])
cityE.addCities([cityF, cityA])
cityF.addCities(([cityB, cityC, cityD, cityE]))


def findCity(letter):
    if letter == "A":
        return cityA
    elif letter == "B":
        return cityB
    elif letter == "C":
        return cityC
    elif letter == "D":
        return cityD
    elif letter == "E":
        return cityE
    elif letter == "F":
        return cityF

def findTotalRoadDistance(city, endCity, distanceSoFar, previousCity, count):

    for i in range(0, len(city.getCities())):

        prevCity = previousCity

        #print(i)
        #print(city.getName())
        #what the city the computer is currently on in the loop
        currentCity = city.getCities()[i]

        #so it doesn't go 'backwards' and check the city where it came from
        if currentCity == prevCity:
            continue

        newDistance = distanceSoFar + findRoadDistance(city, currentCity)
        #print ("distance")
        #print newDistance

        if currentCity == endCity:

            #print("done")
            distances.append(newDistance)
            return distanceSoFar

        else:
            if count < 2:

                findTotalRoadDistance(currentCity, endCity, newDistance, city, count+1)


def findRoadDistance(city, endCity):
    xDistance = city.getX() - endCity.getX()
    yDistance = city.getY() - endCity.getY()

    #print("base city " + city.getName())
    #print("other city " + endCity.getName())

    distance = (xDistance ** 2 + yDistance ** 2)**0.5
    return distance

while True:
    startCity = raw_input("Hello. Please input your which city you would like to start at (A-F). Or input 0 to exit.")
    if (startCity == "0"):
        break

    startCity = startCity.upper()
    endCity = raw_input("Please input the city that would be your destination (A-F).")
    endCity = endCity.upper()
    #if A-F
    if(65 <= ord(startCity) <= 70 and startCity is not endCity and 65 <= ord(endCity) <= 70):
        distances = []
        #The 'O' means object. This is getting the object version of the city
        startCityO = findCity(startCity)
        endCityO = findCity(endCity)

        count = 0
        findTotalRoadDistance(startCityO, endCityO, 0, startCityO, count)

        min = 1000000
        #This loop is to find the shortest distance out of the many possible distances.
        for y in range(0, len(distances)):
            if distances[y] < min:
                min = distances[y]
        print(distances)
        print("")
        print("Your shortest possible distance from City " + startCity + " to City " + endCity + " is: ")
        print(min)

        print("\n\n")


    else:
        print("You entered incorrect input(s). Try again.")


