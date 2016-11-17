import subprocess
import sys

maxIndex = 0
file_out = open("./game.log", "w")
for i in xrange(3):
    subprocess.call(['./runGame.sh'], stdout=file_out)
    sys.stdout.write("Finished Game %d\n" % (i+1))
    game_file = open("./game.log", "r")
    for line in game_file:
        if ("Player" in line):
            sys.stdout.write(line +"\n")


