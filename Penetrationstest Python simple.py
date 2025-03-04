import socket

def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)  # Timeout für langsam reagierende Ports
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} ist offen")
        else:
            print(f"[-] Port {port} ist geschlossen")

# Beispiel-Scan
target_ip = "scanme.nmap.org"  # Oder eine eigene Test-IP
ports = [21, 22, 80, 443, 8080]  # Typische Ports

print(f"Scanne {target_ip}...")
for port in ports:
    scan_port(target_ip, port)
