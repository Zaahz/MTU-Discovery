#!/usr/bin/python
from ofunctions.network import probe_mtu
import sys
import itertools
import threading
import time

done = False
#"progressbar" animation code
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rTesting MTU ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!\r')

t = threading.Thread(target=animate)
t.start()

#fstring variable for new line
new_line = '\n'

#loop for running through all the values supplied to the script
for i in sys.argv[1:]:
	#print (f"{i}")
	print (f"{new_line} {i}: {probe_mtu(i)}")


time.sleep(10)
done = True
