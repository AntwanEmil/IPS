#!/usr/bin/env python3
import subprocess
import os
import time
import re
import sys
import signal
import colorama
from colorama import Fore, Back, Style





print(Fore.RED + '')
print('$$$$$$\ $$$$$$$\   $$$$$$\\')  
print('\_$$  _|$$  __$$\ $$  __$$\ ')
print('  $$ |  $$ |  $$ |$$ /  \__|')
print('  $$ |  $$$$$$$  |\$$$$$$\  ')
print('  $$ |  $$  ____/  \____$$\ ')
print('  $$ |  $$ |      $$\   $$ |')
print('$$$$$$\ $$ |      \$$$$$$  |')
print('\______|\__|       \______/ ')
print(Fore.CYAN + '#### Simple IPS/IDS system created using python/bash ####')
print ('')
print (Fore.YELLOW + 'Choose one of the following options')
print('')
subprocess.call(['sh', './runme.sh'])
while 1:
    print (Fore.YELLOW + '############################')
    print (Fore.YELLOW + '###        IPS/IDS        ##')
    print (Fore.YELLOW + '############################')
    print (Fore.YELLOW + '1:UDP Flooding scan')
    print (Fore.YELLOW + '2:syn Flooding scan')
    print (Fore.YELLOW + '3:icmp Flooding scan')
    print (Fore.YELLOW + '4:DNS Flooding scan')
    print (Fore.YELLOW + '5:Auto scan')
    print ('')

    print (Fore.YELLOW + '############################')
    print (Fore.YELLOW + '###    Firewall Options   ##')
    print (Fore.YELLOW + '############################')
    print (Fore.YELLOW + '6:IP Manual Blacklist/Whitelist')
    print (Fore.YELLOW + '7:MAC Manual Blacklist/Whitelist')
    print (Fore.YELLOW + '8:Specific Port Filtering')
    print (Fore.CYAN + '9:EXIT')
    print(''+ Style.RESET_ALL)
    op = input("")

    if op == '9':
        print (Fore.CYAN + 'EXITING...')
        print(''+ Style.RESET_ALL)
        sys.exit()
    elif op == '1':
        print(Fore.YELLOW +  '### UDP SCAN STARTED (ctrl-c to exit) ###')
        print(''+ Style.RESET_ALL)
        p=subprocess.Popen(['python', './IPS/udp/udp_prev.py'])
        try:
            p.wait()
        except KeyboardInterrupt:
            try:
                p.terminate()
            except OSError:
                pass
            p.wait()
    elif op == '2':
        print(Fore.YELLOW +  '### syn flood SCAN STARTED ###')
        print(''+ Style.RESET_ALL)
        p=subprocess.Popen(['python', './IPS/syn/syn.py'])
        try:
            p.wait()
        except KeyboardInterrupt:
            try:
                p.terminate()
            except OSError:
                pass
            p.wait()
    elif op == '3':
        print(Fore.YELLOW +  '### icmp flood SCAN STARTED ###')
        print(''+ Style.RESET_ALL)
        p=subprocess.Popen(['python', './IPS/icmp/icmp.py'])
        try:
            p.wait()
        except KeyboardInterrupt:
            try:
                p.terminate()
            except OSError:
                pass
            p.wait()
    elif op == '4':
        print(Fore.YELLOW +  '### DNS flood SCAN STARTED ###')
        print(''+ Style.RESET_ALL)
        p=subprocess.Popen(['python', './IPS/dns/dns.py'])
        try:
            p.wait()
        except KeyboardInterrupt:
            try:
                p.terminate()
            except OSError:
                pass
            p.wait()
    elif op == '5':
        print(Fore.YELLOW +  '### AUTO SCAN STARTED ###')
        print(''+ Style.RESET_ALL)
        p=subprocess.Popen(['python', './IPS/auto/auto.py'])
        try:
            p.wait()
        except KeyboardInterrupt:
            try:
                p.terminate()
            except OSError:
                pass
            p.wait()
    elif op == '6':
        print(Fore.YELLOW +  '### IP BLACKLIST/WHITELIST MENU ###')
        print(''+ Style.RESET_ALL)
        subprocess.call(['sh', './Firewall/ip_block.sh'])
    elif op == '7':
        print(Fore.YELLOW +  '### MAC BLACKLIST/WHITELIST MENU ###')
        print(''+ Style.RESET_ALL)
        subprocess.call(['sh', './Firewall/mac_block.sh'])
    elif op == '8':
        print(Fore.YELLOW +  '### PORT FILTERING MENU ###')
        print(''+ Style.RESET_ALL)
        subprocess.call(['sh', './Firewall/port_block.sh'])
