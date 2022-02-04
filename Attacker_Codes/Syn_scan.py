#!/usr/bin/env python

import time
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # Disable the annoying No Route found warning !
from scapy.all import *

ip = "138.68.183.168"

def is_up(ip):
    """ Tests if host is up """
    icmp = IP(dst=ip)/ICMP()
    resp = sr1(icmp, timeout=0.5)
    if resp == None:
        return False
    else:
        return True

def reset_half_open(ip, ports):
    # Reset the connection to stop half-open connections from pooling up
    sr(IP(dst=ip)/TCP(dport=ports, flags='AR'), timeout=1)

def is_open(ip, ports, timeout=0.2):
    results = {port:None for port in ports}
    to_reset = []
    p = IP(dst=ip)/TCP(dport=ports, flags='S')  # Forging SYN packet
    answers, un_answered = sr(p, timeout=timeout)  # Send the packets
    for req, resp in answers:
        if not resp.haslayer(TCP):
            continue
        tcp_layer = resp.getlayer(TCP)
        if tcp_layer.flags == 0x12:
            to_reset.append(tcp_layer.sport)
            results[tcp_layer.sport] = True
        elif tcp_layer.flags == 0x14:
            results[tcp_layer.sport] = False

    # Bulk reset ports
    reset_half_open(ip, to_reset)
    return results

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

if __name__ == '__main__':
    conf.verb = 0 # Disable verbose in sr(), sr1() methods
    start_time = time.time()
    if is_up(ip):
        print ("Host %s is up, start scanning" % ip)
        for ports in chunks(range(1, 2048), 100):
            results = is_open(ip, ports)
            for p, r in results.items():
                print (p, ':', r)
        duration = time.time()-start_time
        print ("%s Scan Completed in %fs" % (ip, duration))
    else:
        print ("Host %s is Down" % ip)