# Host Discovery Service — SDN Project

**Name:** Atharva Anand
**SRN:** PES1UG24CS092
**Course:** UE24CS252B — Computer Networks

---

## 📌 Problem Statement

The objective of this project is to design an SDN-based Host Discovery Service using Mininet and a POX controller.

The controller should:

* Automatically detect hosts joining the network
* Maintain a host database (MAC, IP, port, timestamps)
* Update dynamically based on network traffic
* Install flow rules using match–action logic

---

## 🛠️ Tools & Technologies

* Mininet (Network Emulator)
* POX Controller (OpenFlow SDN controller)
* Open vSwitch (OVS)
* Python 3.13
* Debian Linux (UTM VM)

---

## ⚙️ Setup Instructions

```bash
sudo apt update
sudo apt install mininet git iperf -y
```

Clone POX:

```bash
git clone https://github.com/noxrepo/pox
```

---

## ▶️ How to Run

### Terminal 1 — Start Controller

```bash
cd ~/pox
python3 pox.py forwarding.host_discovery
```

### Terminal 2 — Start Mininet

```bash
sudo python3 ~/host_discovery/topology.py
```

---

## 🧪 Test Commands

Inside Mininet:

### 1. Connectivity Test

```bash
pingall
```

### 2. Flow Table

```bash
sh ovs-ofctl dump-flows s1
```

### 3. Latency Test

```bash
h1 ping -c 4 h2
```

### 4. Throughput Test

```bash
h1 iperf -s &
h2 iperf -c 10.0.0.1
```

---

## 📊 Expected Output

* Hosts are detected dynamically with MAC/IP/Port
* Host database updates in controller logs
* `pingall` shows **0% packet loss**
* Flow rules appear in switch table
* iperf shows bandwidth between hosts

---

## 🧠 SDN Concepts Used

* **Packet-In Handling:** Controller processes incoming packets
* **Match-Action Rules:** Flow rules installed dynamically
* **Learning Switch:** MAC-to-port mapping maintained
* **Dynamic Host Discovery:** Hosts detected automatically

---

## 📸 Screenshots

<img width="774" height="366" alt="Screenshot 2026-04-10 at 12 13 40 AM" src="https://github.com/user-attachments/assets/28fb380a-8f10-4c7a-a5ac-927b8d71acb3" />

---

## 📈 Performance Analysis

* **Latency:** Measured using ping (ms)
* **Throughput:** Measured using iperf (Mbps/Gbps)
* **Flow Rules:** Observed via OVS flow table

---

## 📚 References

* https://mininet.org/walkthrough/
* https://noxrepo.github.io/pox-doc/html/
* OpenFlow Specification v1.0

---

## ✅ Conclusion

The project successfully demonstrates SDN-based host discovery using a POX controller.
Dynamic flow rule installation improves efficiency by reducing controller involvement after initial packets.

---
