#!/bin/bash

echo "Block Any specific port of your choice (1->65534)"
echo
echo "1: Close Inbound Port"
echo "2: Close Outbound Port"
echo "3: Open TCP Inbound Port"
echo "4: Open UDP Port(udp is uni-directional)"
echo "5: Exit "
echo
read NUM
if [ "$NUM" -eq 1 ]; then 
        echo "What is Port number you want to protect from inbound connections: "
        read Po
        iptables -A INPUT -p tcp --destination-port $Po -j DROP
        echo "##Inbound Port Blocked"
elif [ "$NUM" -eq 2 ]; then
        echo "Port will be disallowed from making outgoing traffic (req to untrusted websites):"
        echo
        echo "Port Number: "
        read p2
        iptables -A OUTPUT -p tcp --dport $p2 -j DROP
        echo "##Outbound Port Blocked"


elif [ "$NUM" -eq 3 ]; then
        echo "Port Number : "
        read p3
        iptables -I INPUT -p tcp --dport $p3 -j ACCEPT
        iptables -I INPUT -p tcp --dport $p3 --syn -j ACCEPT
        echo "##port Opened for Inbound connections"
elif [ "$NUM" -eq 4 ]; then
        echo "Port Number: "
        read p4
        iptables -I INPUT -p udp --dport $p4 -j ACCEPT
        echo "Port opened successfully"


elif [ "$NUM" -eq 5 ]; then
        exit 0
else
        echo "ERR 2: NOT SUPPORTED OPTION"
        echo "closing"
        exit 0
fi