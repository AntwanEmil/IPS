#!/bin/bash

echo "This Allows you to Manually blacklist/whitelist any MAC Address "
echo
echo "1: Blacklist MAC-Addr"
echo "2: Whitelist MAC-Addr"
echo "3: Exit"
echo
read NUM
if [ "$NUM" -eq 1 ]; then 
        echo "MAC Addr to be blocked : "
        read mac
        iptables -A INPUT -m mac --mac-source $mac -j DROP
        iptables -A FORWARD -m mac --mac-source $mac -j DROP
        echo "Give MAC-Addr blacklisted"
elif [ "$NUM" -eq 2 ]; then
        echo "MAC-Addr to be whitelisted:"
        read al
        iptables -I INPUT -m mac --mac-source $al -j ACCEPT
        echo "MAC-Addr whitelisted "

elif [ "$NUM" -eq 3 ]; then
        exit 0
else
        echo "ERR 2: NOT SUPPORTED OPTION"
        echo "closing"
        exit 0
fi