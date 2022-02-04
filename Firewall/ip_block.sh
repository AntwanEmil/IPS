#!/bin/bash

echo "This Allows you to Manually blacklist/whitelist any IP"
echo
echo "1: Blacklist IP"
echo "2: Whitelist IP"
echo "3: Exit"
echo
read NUM
if [ "$NUM" -eq 1 ]; then 
        echo "Ip: "
        read ip
        iptables -A INPUT -s $ip -j DROP
        iptables -A INPUT -s $ip -p tcp --destination-port 80 -j DROP
        iptables -A INPUT -s $ip -p tcp --destination-port 443 -j DROP
        sudo ufw deny from $ip 
        echo "## Given IP won't be able to communicate again through common ports"
elif [ "$NUM" -eq 2 ]; then
        echo "IP to remove from blacklist : "
        read ip2
        iptables -D INPUT -s $ip2 -j DROP
        sudo ufw allow from $ip2
        echo "## Given IP is removed from blacklisted IPs"
elif [ "$NUM" -eq 3 ]; then
        exit 0
else
        echo "ERR 2: NOT SUPPORTED OPTION"
        exit 0
fi