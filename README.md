# Automated Network Vulnerability Scanner

A Python-based DevSecOps network security tool that discovers active hosts on a subnet, scans open ports and running services, cross-references known CVEs via the Nmap Scripting Engine (NSE), and exports structured JSON audit reports.

## Architecture & Tech Stack
* **Language:** Python 3
* **Environment:** Kali Linux
* **Network Discovery:** `scapy` (Layer 2 ARP broadcast sweeping)
* **Vulnerability Engine:** `python-nmap` with Nmap NSE (`--script vuln`)
* **Reporting:** Structured JSON output for CI/CD and security pipeline ingestion

## Key Features
* **Subnet Discovery:** Uses raw ARP requests across `/24` subnets to identify live IP and MAC addresses, bypassing basic ICMP ping blocks.
* **Stealth Scanning & Fingerprinting:** Runs TCP SYN scans (`-sS`) and service version detection (`-sV`) on discovered hosts.
* **Automated CVE Mapping:** Matches detected service banners against Nmap vulnerability scripts and exploit databases.
* **JSON Audit Reports:** Saves timestamped per-target scan results cleanly to disk.

## Setup & Usage
*Requires root privileges for raw ARP and SYN packet crafting.*

```bash
git clone [https://github.com/SHEDGEADITYA/network-vuln-scanner.git](https://github.com/SHEDGEADITYA/network-vuln-scanner.git)
cd network-vuln-scanner

python3 -m venv venv
source venv/bin/activate
pip install python-nmap scapy

sudo ./venv/bin/python scanner.py



Disclaimer
Built strictly for authorized security testing, lab environments, and defensive DevSecOps workflows. Only scan networks and hosts you own or have explicit written permission to test.

*Verification:* Click the **Preview** tab at the top-left of the editor to confirm the headings, bullet points, and code block format cleanly.
