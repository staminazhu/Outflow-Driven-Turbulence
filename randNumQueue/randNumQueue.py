#!/bin/env python

import Queue, time, sys

def do_queue(n):
  start = time.time()
  q = Queue.Queue(1000)
  for i in range(n):
    try:
      a = q.get_nowait()
    except Queue.Empty, e:
      fid = file("rand.txt")
      for x in range(500):
        q.put_nowait(float(fid.readline().strip()))
      fid.close()
  return time.time() - start
      
def do_file(n):
  start = time.time()
  fid = file("rand.txt")
  for x in range(n):
    try:
      a = float(fid.readline().strip())
    except Exception, e:
      fid.close()
      fid = file("rand.txt")
      a = float(fid.readline().strip())
      
  return time.time() - start
  
  
qtimes = []
ftimes = []
print "Starting the trial"
for n in range(1000,3000,500):
  if n%500 == 0:
    print "%d,"%n,
    sys.stdout.flush()
  qtimes.append(do_queue(n))
  ftimes.append(do_file(n))
  
# print "Making Graph"
# from pylab import *
# clf()
# plot(range(1000),qtimes,label="Queue")
# plot(range(1000),ftimes,label="File")
# title("Benchmark");
# xlabel("# of randoms queried")
# show()

import numpy
q = numpy.array(qtimes)
f = numpy.array(ftimes)