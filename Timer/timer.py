#!/usr/bin/python

import datetime
import signal, sys, time

start = datetime.datetime.now()
def signal_handler(signal, frame):
  print ('\nstopping\n')

  time.sleep(0.1)
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
#signal.pause() # does not work under Windows
while(True):
    timelaps = datetime.datetime.now() - start
    sys.stdout.write("\r{0}".format(timelaps))
    sys.stdout.flush()
    time.sleep(0.1)
