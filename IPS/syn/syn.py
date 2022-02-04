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
    stream = os.popen('tcpdump -c 10 -i eth0 "tcp[tcpflags] & (tcp-syn|tcp-ack) != 0" >> syn.txt 2> /dev/null')
    time.sleep(5)



    print ("\t\tscanning for syn flooding (stealth flooding)....")


    flag =0
    old_ip = "0.0.0.0"
    file = open("syn.txt", "r")
    for line in file:
            try:
                    ip=re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line).group()
                    home = "198"
                    if ip in blocked_ips or not ip or ip[0:3] == "198":
                        continue
                    if old_ip == ip:
                            flag += 1
                            print(ip)
                            print (flag)
                    else:
                            flag =0
                    old_ip = ip
                    if flag == 9:
                            print('########syn flood detected from ip: {}'.format(ip));
                            ## calling the bash script to blacklist this ip
                            blck = 'iptables -A INPUT -s ' + ip + ' -j DROP'
                            os.popen(blck)
                            p = subprocess.Popen(["iptables", "-A", "INPUT", "-s", ip,"-j", "DROP"], stdout=subprocess.PIPE)
                            #blck= 'iptables -A INPUT -s ' +ip +'-p tcp --destination-port 80 -j DROP'
                            #os.popen(blck)
                            subprocess.Popen(["iptables", "-A", "INPUT", "-s",ip ,"-j" , "DROP"] ,stdout=subprocess.PIPE) 
                            #blck = 'iptables -A INPUT -s ' +ip +'-p tcp --destination-port 443 -j DROP'
                            #os.popen(blck)
                            blck  = 'sudo ufw deny from ' + ip
                            os.popen(blck) 
                            print('########this ip is auto-blocked from further communication')
                            blocked_ips.append(ip)
                            break
            except Exception as e:
                    flag = 0
