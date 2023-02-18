import os

ipv4 = open("ips-v4.txt", "r")

ipv4 = ipv4.read().split("\n")

for i in ipv4:
    os.system(f"ufw allow from {i} proto tcp to any port 80")
    os.system(f"ufw allow from {i} proto tcp to any port 443")

ipv6 = open("ips-v6.txt", "r")

ipv6 = ipv6.read().split("\n")

for i in ipv6:
    os.system(f"ufw allow from {i} proto tcp to any port 80")
    os.system(f"ufw allow from {i} proto tcp to any port 443")