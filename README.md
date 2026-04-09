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

<img width="757" height="392" alt="Screenshot 2026-04-10 at 12 22 07 AM" src="https://github.com/user-attachments/assets/dee2b84e-3a18-493e-be71-af1671f84453" />

<img width="894" height="779" alt="Screenshot 2026-04-10 at 12 38 40 AM" src="https://github.com/user-attachments/assets/c839526c-c5ac-4d52-a622-b08a894753b7" />

<img width="1496" height="776" alt="Screenshot 2026-04-10 at 1 02 03 AM" src="https://github.com/user-attachments/assets/9c920003-85f5-4093-963f-f22075387e24" />

<img width="1509" height="293" alt="Screenshot 2026-04-10 at 1 03 32 AM" src="https://github.com/user-attachments/assets/57861451-0f45-4901-b449-25b33be45107" />

<img width="908" height="766" alt="Screenshot 2026-04-10 at 12 32 08 AM" src="https://github.com/user-attachments/assets/2f98476e-e2d3-493b-8cf0-adef6ca576de" />

<img width="774" height="366" alt="Screenshot 2026-04-10 at 12 13 40 AM" src="https://github.com/user-attachments/assets/f21fd751-6703-403b-a764-dce7f1cfd573" />

<img width="948" height="581" alt="Screenshot 2026-04-10 at 12 14 06 AM" src="https://github.com/user-attachments/assets/d8034f58-258f-461f-af90-a947ef2d5601" />

<img width="373" height="165" alt="Screenshot 2026-04-10 at 12 16 55 AM" src="https://github.com/user-attachments/assets/93f530eb-90ef-4435-8f6a-4598deff35aa" />

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
