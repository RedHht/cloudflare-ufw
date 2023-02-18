# "Cloudflare-ufw"
Simple Python script that adds every single cloudflare reverse proxy ip (v4 and v6) to your ufw firewall so every connection to ports 443 or 80 MUST be from Cloudflare's proxyes.

This python script can run in any distro that has ufw installed and enabled, by default ufw has the policy for incoming connections stablished on  "drop", so every connection to port 80 and 443 will be just... "burned" so if you run this script when the firewall is configured with default, this script will work flawlessly but if you touched the firewall, make sure that you dont have any rules like "ufw allow to proto tcp 80", first delete any rules associated with port 80 or 443 and run the script.

All necesary files are in the src folder, it contains a list of the Ipv4 and another list of Ipv6 of cloudflare, if you want you can download you owns from https://www.cloudflare.com/ips/, only make sure that this IP lists have the same name for the script to work.
