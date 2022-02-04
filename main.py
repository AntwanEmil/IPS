#!/usr/bin/env python3
import subprocess
import os
import time
import re
import sys

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
    print (Fore.YELLOW + 'EXITING...')
    sys.exit()
elif op == '1':
    print(Fore.YELLOW +  '### UDP SCAN STARTED ###')
    print(''+ Style.RESET_ALL)
    subprocess.call('IPS/udp/udp_prev.py', shell=True)