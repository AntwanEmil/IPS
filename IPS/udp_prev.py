#!/usr/bin/env python3

import subprocess
print "start of scan ..."
while 1:
    subprocess.call("tcpdumbudp.sh")
    #open the output file
    #parse
    #inner for loop on the file contents (with a flag)
    ## if found 10 consec bla bla break and set break flag =1
    # break
    

print "end"
