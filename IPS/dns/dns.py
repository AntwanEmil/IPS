#!/usr/bin/env python3
import subprocess
import os
import time
import re

blocked_ips = [""];
while 1:
    stream = os.popen('tcpdump -c 50 -i eth0 -nnn port 53 and not port 22>> dns.txt 2> /dev/null')
    time.sleep(10)



    print ("\t\tscanning for DNS flooding....")


    flag =0
    old_ip = "0.0.0.0"
    file = open("dns.txt", "r")
    for line in file:
            try:
                    ip=re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line).group()
                    if ip in blocked_ips:
                        continue
                    if old_ip == ip:
                            flag += 1
                    else:
                            flag =0
                    old_ip = ip
                    if flag == 10:
                            print('########DNS flooding detected from ip: {}'.format(ip));
                            ## calling the bash script to blacklist this ip
                            blck = 'iptables -A INPUT -s ' + ip + ' -j DROP'
                            os.popen(blck)
                            p = subprocess.Popen(["iptables", "-A", "INPUT", "-s", ip,"-j", "DROP"], stdout=subprocess.PIPE)
                            blck= 'iptables -A INPUT -s ' +ip +'-p tcp --destination-port 80 -j DROP'
                            os.popen(blck) 
                            blck = 'iptables -A INPUT -s ' +ip +'-p tcp --destination-port 443 -j DROP'
                            os.popen(blck)
                            blck  = 'sudo ufw deny from ' + ip
                            os.popen(blck) 
                            print('########this ip is auto-blocked from further communication')
                            blocked_ips.append(ip)
                            break
            except Exception as e:
                    flag = 0
