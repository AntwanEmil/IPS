#!/usr/bin/env python3
import subprocess
import os
import time
import re
import signal


def handler(signum, frame):
        exit(1)

signal.signal(signal.SIGINT, handler)
blocked_ips = [""];
while 1:
    stream = os.popen('tcpdump -c 10 -i eth0 icmp >> icmp.txt 2> /dev/null')
    time.sleep(5)




    print ("\t\tscanning for icmp flooding....")


    flag =0
    old_ip = "0.0.0.0"
    file = open("icmp.txt", "r")
    for line in file:
            try:
                    ip=re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line).group()
                    host = re.search(r'\bhost-\b',strs).group(0)
                    if ip in blocked_ips or if not host:
                        continue
                    if old_ip == ip:
                            flag += 1
                    else:
                            flag =0
                    old_ip = ip
                    if flag == 9:
                            print('########icmp attack detected from ip: {}'.format(ip));
                            ## calling the bash script to blacklist this ip
                            blck = 'iptables -A INPUT -s ' + ip + ' -j DROP'
                            os.popen(blck)
                            p = subprocess.Popen(["iptables", "-A", "INPUT", "-s", ip,"-j", "DROP"], stdout=subprocess.PIPE)
                            #blck= 'iptables -A INPUT -s ' +ip +'-p tcp --destination-port 80 -j DROP'
                            #os.popen(blck)
                            subprocess.Popen(["iptables", "-A", "INPUT", "-p" ,"tcp","-s",ip ,"-j" , "DROP"] ,stdout=subprocess.PIPE) 
                            #blck = 'iptables -A INPUT -s ' +ip +'-p tcp --destination-port 443 -j DROP'
                            #os.popen(blck)
                            subprocess.Popen(["ufw" , "deny" , "from" , ip] ,stdout=subprocess.PIPE)

                            print('########this ip is auto-blocked from further communication')
                            blocked_ips.append(ip)
                            break
            except Exception as e:
                    flag = 0
