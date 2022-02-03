#!/usr/bin/env python3
import subprocess
import os
import time
stream = os.popen('tcpdump -c 10 -i eth0 udp > udp.txt 2> /dev/null')
#p = subprocess.Popen(
#        ['tcpdump', '-i', ifname, '-w', '-', filter],
#        stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
time.sleep(5)

#p.terminate()

#print (output)

print ("end")



f = open("udp.txt", "r")
print(f.read())
