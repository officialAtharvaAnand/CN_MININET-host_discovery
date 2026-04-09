# Host Discovery Service — SDN Project
**Name:** Atharva Anand  
**SRN:** PES1UG24CS092  
**Course:** UE24CS252B — Computer Networks

## Problem Statement
Automatically detect and maintain a database of all hosts joining an SDN network.
The POX controller detects host join events via packet_in, records MAC/IP/port/timestamp,
and updates the host database dynamically.

## Tools Used
- Mininet (network emulator)
- POX Controller (OpenFlow SDN controller)
- Open vSwitch
- Python 3.13 / Debian 13

## Setup Instructions
1. Install Mininet: `sudo apt install mininet -y`
2. Clone POX: `git clone https://github.com/noxrepo/pox`
3. Copy `host_discovery.py` into `~/pox/pox/forwarding/`

## How to Run
**Terminal 1 — Start POX controller:**
```bash
cd ~/pox
python3 pox.py forwarding.host_discovery
```

**Terminal 2 — Start Mininet topology:**
```bash
sudo python3 topology.py
```

**Inside Mininet CLI:**
