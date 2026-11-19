import nmap
import sys
import json
from datetime import datetime

def run_vuln_scan(target_ip):
    print(f"\n[*] Starting Vulnerability scan on {target_ip}...")
    scanner = nmap.PortScanner()
    
    # Initialize the JSON report structure
    report_data = {
        "scan_time": str(datetime.now()),
        "target": target_ip,
        "open_ports": []
    }
    
    try:
        scanner.scan(target_ip, arguments='-sS -sV --script vuln -p 1-1000')
    except Exception as e:
        print(f"[-] Scan failed: {e}")
        sys.exit(1)
        
    for host in scanner.all_hosts():
        print(f"\n[+] Target: {host}")
        
        for protocol in scanner[host].all_protocols():
            ports = scanner[host][protocol].keys()
            
            for port in sorted(ports):
                state = scanner[host][protocol][port]['state']
                service = scanner[host][protocol][port]['name']
                version = scanner[host][protocol][port].get('version', '')
                
                print(f"\n[>] Port: {port} | State: {state} | Service: {service} {version}")
                
                # Create a dictionary for this specific port
                port_info = {
                    "port": port,
                    "state": state,
                    "service": f"{service} {version}".strip(),
                    "vulnerabilities": []
                }
                
                if 'script' in scanner[host][protocol][port]:
                    print("    [!] Vulnerabilities / Notes Found:")
                    for script_name, script_output in scanner[host][protocol][port]['script'].items():
                        print(f"      --- {script_name.upper()} ---")
                        
                        # Add vulnerability details to our report list
                        port_info["vulnerabilities"].append({
                            "script": script_name,
                            "output": script_output.strip()
                        })
                        
                        for line in script_output.split('\n'):
                            print(f"        {line}")
                else:
                    print("    [-] No obvious vulnerabilities detected.")
                
                # Append the port info to the main report
                report_data["open_ports"].append(port_info)

    # Save the report to a JSON file
    filename = f"scan_report_{target_ip.replace('.', '_').replace('/', '_')}.json"
    with open(filename, 'w') as f:
        json.dump(report_data, f, indent=4)
        
    print(f"\n[+] Scan complete. Report saved to {filename}")

if __name__ == "__main__":
    target = input("Enter Target IP to scan (e.g., 127.0.0.1): ")
    run_vuln_scan(target)
