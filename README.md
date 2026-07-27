# Cyber-Security-Projects
# Project 01 - Network Port Scanner

## What it Does 
Scans a target IP or hostname for open TCP ports and identifies running services. Built as a foundational network reconnaissance tool - the same core concept behind Nmap.

## What I Learned 
- How TCP connections work at code level 
- Socket programming in Python
- How port scanning works under the hood
- Port to service mapping (HTTP=80, SSH=22, HTTPS=443 etc.)

## Concepts Covered 
- TCP handshake mechanism 
- Network reconnaissance fundamentals
- Python socket library 
- Error handling and timeouts 

## Tools & Languages 
- Python 3
- Socket library (built-in)

## How to run
'''bash
python3 port_scanner.py
'''

Then enter a target hostname and port range when prompted.

## Legal Notice 
Only use this tool on networks and systems you own or have explicit written permission to scan. Unauthorized port scanning is illegal in most jurisdictions.

## Example Output 
'''
Target :    scanme.nmap.org (45.33.32.156)
Port Range : 1 - 100
---------------------------------------------------

PORT            SERVICE            STATUS

---------------------------------------------------
22              SSH                 OPEN
80              HTTP                OPEN
---------------------------------------------------

Scan complete. 2 open ports found.
'''