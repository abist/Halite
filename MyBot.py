from hlt import *
from networking import *

myID, gameMap = getInit()
sendInit("PythonBot")

def move(x,y):
    location = Location(x, y)
    site = gameMap.getSite(location)
    for d in CARDINALS:
        neighbour_site = gameMap.getSite(location, d)
        if neighbour_site.owner != myID and neighbour_site.strength < site.strength:
            return Move(location, d)

    neighbours = []
    for d in CARDINALS:
        for i in range(-1,2,1):
            for j in range(-1,2,1):
                neighbours.append(gameMap.getSite(Location(i,j), d))

    surrounded = True
    for neighbour in neighbours:
        if (neighbour.owner != myID):
            surrounded = False
            break

    if (surrounded):
        return Move(location, NORTH if random.random() > 0.5 else WEST)

    if site.strength < site.production * 5:
        return Move(location, STILL)

    return Move(location, NORTH if random.random() > 0.5 else WEST)

while True:
    moves = []
    gameMap = getFrame()
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            location = Location(x, y)
            if gameMap.getSite(location).owner == myID:
                moves.append(move(x,y))
    sendFrame(moves)