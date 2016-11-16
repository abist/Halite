import subprocess
import sys

file_out = open("./game.log", "w")
for i in xrange(10):
    subprocess.call(['./runGame.sh'], stdout=file_out)
    sys.stdout.write("Finished Game %d\n" % (i+1))


