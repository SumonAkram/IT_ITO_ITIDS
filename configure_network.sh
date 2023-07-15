#!/bin/bash

# Configure network settings
network_interface="eth0"
ip_address="192.168.1.100"
netmask="255.255.255.0"
gateway="192.168.1.1"
dns_servers="8.8.8.8 8.8.4.4"

echo "Configuring network interface $network_interface..."
sudo ifconfig $network_interface $ip_address netmask $netmask up
sudo route add default gw $gateway

# Configure DNS servers
echo "Configuring DNS servers..."
sudo sh -c "echo 'nameserver $dns_servers' >> /etc/resolv.conf"

echo "Network configuration complete."
